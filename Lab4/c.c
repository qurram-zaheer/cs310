#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include<sys/types.h>

#define PORT 9003



int main(int argc, char* argv[]){
  int network_socket;

  if ((network_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0 ){
    perror("Socket Failed!\n");
    exit(EXIT_FAILURE);
  };

  struct sockaddr_in servaddr;
  servaddr.sin_family = AF_INET;
  servaddr.sin_port = htons(PORT);
  servaddr.sin_addr.s_addr = INADDR_ANY;

  if (connect(network_socket, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0 ) {
    perror("Connection Failed!\n");
    exit(EXIT_FAILURE);
  }

  char server_response[256];
  char filename[40];
  printf("Enter the string\n");
  fgets(filename, 40, stdin);

  printf("%s\n",filename);
  int i = 0;
  int *tempArray = (int*)malloc(40*sizeof(int));
  for (int j = 0;j < 40; j++){
    tempArray[j] = 300;
  }
  char *c = filename;
  while (*c != NULL){
    printf("%d:\t%c\n",i,*c);
    tempArray[i] = *c;
    c++;
    i++;
  }
  int value;
  int rem;
  int **ascii_array = (int**)malloc((i-1)*sizeof(int*));
  for (int j = 0;j < (i-1); j++){
    printf("%d  ", tempArray[j]);
    value = tempArray[j];
    ascii_array[j] = (int *)malloc(8*sizeof(int));
    for (int k = 0;k < 8; k++){
      rem = value%2;
      ascii_array[j][7-k] = rem;
      value = value/2;
    }
  }
  printf("\n");

  for(int j = 0;j < (i-1);j++){
    for (int k =0;k<8;k++){
      printf("%d ",ascii_array[j][k]);
    }
    printf("\n");
  }
  
  read(network_socket, server_response, 256);
  printf("The server replied with\n%s\n", server_response);
  int **buffer = (int **)malloc(i*sizeof(int*));
  
  for (int j = 0;j<i;j++){
    buffer[j] = (int*)malloc(8*sizeof(int));
    if (j == 0){
      buffer[j][0] = i-1;
    }
  }

  for (int j = 0; j < (i-1); j ++){
    for (int k= 0;k < 8;k++){
      buffer[j+1][k] = ascii_array[j][k];
    }
  }
  for (int j = 0; j < i; j ++){
    for (int k= 0;k < 8;k++){
      printf("%d ", buffer[j][k]);
    }
    printf("\n");
  }

  if (send(network_socket, ascii_array, sizeof(ascii_array),0) < 0){
    perror("Sending failed!\n");
    exit(EXIT_FAILURE);
  }

  close(network_socket);

  return 0;

}