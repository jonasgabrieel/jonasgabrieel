//Projeto de PI 2 
//Alunos: Jonas Gabriel dos Santos Ribeiro
//        Almir Vinicuis Bispo do Nascimento

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX 30
//struct que gera o vetor alunos.
struct cadastro {
    int matricula, codigoTurma, faltas;
    float notas[4];
    char nome[200];
} alunos[MAX];

// DEclaração de funções utilizadas
int qtdade = 0;
void escreverAluno(struct cadastro estudante[]);
void lerArquivo(struct cadastro estudante[]);
bool verificarLimite(struct cadastro estudante[]);
bool matriculaErrada(int num);
bool matriculaExistente(struct cadastro estudante[], int num);
bool matriculaNaoExistente(struct cadastro estudante[], int num);
void funcPrint(void);
void cadastrarAluno(struct cadastro estudante[]);
void removerAluno(struct cadastro estudante[]);
void atualizaAluno(struct cadastro estudante[]);
void apresentaAluno(struct cadastro estudante[]);
void apresentaAprov(struct cadastro estudante[]);
void apresentaReprovMedia(struct cadastro estudante[]);
void apresentaReprovFalta(struct cadastro estudante[]);
float mediaAluno (struct cadastro estudante[], int num);
int len(struct cadastro estudante[]);
void trocaTroca(struct cadastro vetor[], int len1, int len2);
void borbulharNome(struct cadastro vetor[], int len);
void borbulharMedia(struct cadastro vetor[], int len);
void borbulharFalta(struct cadastro vetor[], int len);
void borbulharMatricula(struct cadastro vetor[], int len);
void orgoniza(struct cadastro estudante[]);

//Função Principal
int main(void){
int opcao;
    for(int i = 0; i< MAX; i++){
        alunos[i].matricula = 0;
    }

	lerArquivo(alunos);

    while (opcao != 9) {
    
        funcPrint();
    
        scanf("%i", &opcao);

        switch (opcao){
             
            case 1 :   
                cadastrarAluno(alunos);
            break;

            case 2:
                removerAluno(alunos);
            break;

            case 3:
                atualizaAluno(alunos);
            break;

            case 4 : 
                apresentaAluno(alunos);
            break;
            
            case 5 :
                apresentaAprov(alunos);
            break;
            
            case 6 :
                apresentaReprovMedia(alunos);
            break;
            
            case 7:
                apresentaReprovFalta(alunos);
            break;
            
            case 8:
                orgoniza(alunos);
            break;

            case 9:
                printf("Fim do Programa!");                      	escreverAluno(alunos);

            break;
            
            default:
                printf("O valor Digitado não é reconhecido pelo sistema,tente novamente. \n\n");
        }
    }

	//escreverAluno(alunos);

    return 0;
} 

// funcoes utilizadas
//função de apoio print seu objetivo é sempre printar o menu de opções na tela.
void funcPrint(void){
    printf("[Digite 1 para cadastrar um aluno] : \n\n");
    printf("[Digite 2 para remover um aluno]: \n\n");
    printf("[Digite 3 para atualizar os dados do aluno]: \n\n");
    printf("[Digite 4 para apresentar alunos cadastrados]: \n\n");
    printf("[Digite 5 para apresentar alunos aprovados]: \n\n");
    printf("[Digite 6 para apresentar alunos reprovados por media]: \n\n");
    printf("[Digite 7 para apresentar alunos reprovados por falta]: \n\n");
    printf("[Digite 8 para ordenar]: \n\n");
    printf("[Digite 9 para sair]: \n\n");
}
//Função de Apoio que calcula a media de todos os alunos
float mediaAluno(struct cadastro estudante[], int num){
    float soma = 0;

    for(int i = 0; i < 4; i++){
        soma += estudante[num].notas[i];
    }

    return (soma / 4);
}

//Funções de erro
//Função de erro caso a turma cadastrada não exista
bool turmaNaoExistente(struct cadastro estudante[], int num){
    bool t = true;

     for(int i = 0; i < MAX;i++){
        if(estudante[i].codigoTurma == num){
            t = false;
        }
    }
    return t;
}
//Função de erro caso o limite de alunos seja exedido
bool verificarLimite(struct cadastro estudante[]){
    bool t = true;
    
    for(int i = 0; i < MAX; i++ ){
        if(estudante[i].matricula == 0){
            t = false;
        }
    }
    return t;
}
// Função de erro caso a matricula seja informada de forma errada
bool matriculaErrada(int num){
    bool t = true;
    
    if( num > 2021000 && num < 2021100 ){
        t = false;
    }
    return t;
}
// Função de erro caso a matricula informada já estiver cadastrada no vetor
bool matriculaExistente(struct cadastro estudante[], int num){
    bool f = false;

    for(int i = 0; i < MAX;i++){
        if(estudante[i].matricula == num){
            f = true;
        }
    }
    return f;
}
//Função de erro caso a matricula não tenha sido cadastrada no vetor
bool matriculaNaoExistente(struct cadastro estudante[], int num){
    bool t = true;

     for(int i = 0; i < MAX;i++){
        if(estudante[i].matricula == num){
            t = false;
        }
    }
    return t;
}

// Funções do menu de opções
//Função que cadastra o aluno e seus dados no vetor
void cadastrarAluno(struct cadastro estudante[])
{
    int num;
    
    if(verificarLimite(estudante)){
        printf("[Limite de cadastros atingido, tente novamente]\n");
    } else {
        printf("[Informe a matricula]: ");
        scanf("%i", &num);
        
        if(matriculaErrada(num)){
            printf("\n[Erro! Matricula digitada de forma incorreta, tente outra vez]\n\n");
        } else if(matriculaExistente(estudante, num)){
            printf("[Erro! Matricula ja existe, tente novamente]\n");
        } else {
            
            for(int i = 0; i < MAX; i++){
                if(estudante[i].matricula == 0){
                    estudante[i].matricula = num;
                    for(int j = 0; j < 4; j++){
                        printf("[Informe a nota %i]: ", j+1);
                        scanf("%f", &estudante[i].notas[j]);
                    }
                    printf("[Informe o nome do aluno]:");
                    scanf(" %[^\n]", estudante[i].nome); 
                    
                    printf("[Informe o codigo da turma]:");
                    scanf("%i", &estudante[i].codigoTurma);
                    
                    printf("[Informe a quantidade de faltas]:");
                    scanf("%i", &estudante[i].faltas);

                    
                    break;
                }
            }
            printf("\nMatricula cadastrada com sucesso!\n\n");
        }
    }
    
}
//Função remove aluno do vetor juntamente com seus dados.
void removerAluno(struct cadastro estudante[]){
    int num;

    printf("[Informe a matricula]: ");
    scanf("%i", &num);

    if(matriculaErrada(num)){
        printf("\n[Erro! Matricula digitada de forma incorreta, tente outra vez]\n\n");
    } else {
        if(matriculaNaoExistente(estudante, num)){
        printf("Matricula não existe, tente novamente.\n");
        } else {
            for (int i = 0; i < MAX; i++){
                if(estudante[i].matricula == num){
                    estudante[i].matricula = 0;
                    estudante[i].notas[0] = 0;
                    estudante[i].notas[1] = 0;
                    estudante[i].notas[2] = 0;
                    estudante[i].notas[3] = 0;
                    estudante[i].faltas = 0;

                    printf("Aluno removido com sucesso.\n");
                }
            }
        }
    }
}
//Função que atualiza todos os dados do aluno,exeto a matricula.
void atualizaAluno(struct cadastro estudante[]){
    int num;

    printf("[Informe a matricula]: ");
    scanf("%i", &num);

 if(matriculaErrada(num)){
        printf("\n[Erro! Matricula digitada de forma incorreta, tente outra vez]\n\n");
    } else {
        if(matriculaNaoExistente(estudante, num)){
        printf("Matricula não existe, tente novamente.\n");
        } else {
            for (int i = 0; i < MAX; i++){
                if(estudante[i].matricula == num){
                    for(int j = 0; j < 4; j++){
                        printf("[Informe a nota %i]: ", j+1);
                        scanf("%f", &estudante[i].notas[j]);
                    }
                    printf("[Informe o nome do aluno]:");
                    scanf(" %[^\n]", estudante[i].nome); 
                    
                    printf("[Informe o codigo da turma]:");
                    scanf("%i", &estudante[i].codigoTurma);
                    
                    printf("[Informe a quantidade de faltas]:");
                    scanf("%i", &estudante[i].faltas);


                    printf("Aluno atualizado com sucesso.\n");

                }
            }
        }
    }
}
//Função que apresenta todos os alunos cadastrados no vetor 
void apresentaAluno(struct cadastro estudante[]){
    int num;

    printf("[Informe a turma]: ");
    scanf("%i", &num);
    if (turmaNaoExistente(estudante,num)){                                  
        printf("Turma não existe.");

    } else {
        for (int i = 0; i < MAX; i++) {
            if (estudante[i].matricula != 0 && estudante[i].codigoTurma == num) {
                printf("\nAluno %i\nMatricula: [%i]\n", i + 1, estudante[i].matricula);
                printf("Nome do aluno: %s\n", estudante[i].nome);
                printf("Notas %i: %.2f\n", 1, estudante[i].notas[0]);
                printf("Notas %i: %.2f\n", 2, estudante[i].notas[1]);
                printf("Notas %i: %.2f\n", 3, estudante[i].notas[2]);
                printf("Notas %i: %.2f\n", 4, estudante[i].notas[3]);
                printf("Faltas: %i\n", estudante[i].faltas);
            }
        }  
    }
    

      printf("\n");  
}
//Função que apresenta os alunos de uma turma reprovados por media.
void apresentaReprovMedia(struct cadastro estudante[]){
    int num;

    printf("[Informe a turma]: ");
    scanf("%i", &num);

    if (turmaNaoExistente(estudante,num))                                  
        printf("Turma não existe.");
    else {
        for(int i = 0; i < MAX; i++){
            float media;
            if(estudante[i].codigoTurma == num){
                media = mediaAluno(estudante, i);
                if(media < 7)
                     printf("\nNome: %s \nMatricula: %i \nMedia: %.2f\n\n",estudante[i].nome ,estudante[i].matricula, media);
            }   
        }
    }
}
//Função que apresenta alunos de uma turma reprovados por falta
void apresentaReprovFalta(struct cadastro estudante[]){
    int entrada;
    
    printf("[Informe a turma];");
    scanf("%i", &entrada);

    if(turmaNaoExistente(estudante,entrada))
        printf("Turma não existe.");

    else{
        for(int i = 0; i < MAX; i++){
            if(estudante[i].codigoTurma == entrada)
                if(estudante[i].faltas >= 22){
                    printf("\nNome: %s\nMatricula: %i \nMedia: %i\n\n",estudante[i].nome ,estudante[i].matricula, estudante[i].faltas);
                }
        }
    }
   

}
//Função que apresenta todos os alunos aprovados 
void apresentaAprov(struct cadastro estudante[]){
    int acesso;

    printf("[Informe a turma];");
    scanf("%i", &acesso);

    if(turmaNaoExistente(estudante, acesso))
        printf("Turma não existe.");
    else{
        for(int i = 0;i < MAX;i++){
            float media;
            if(estudante[i].codigoTurma == acesso){
                media = mediaAluno(estudante, i);
                if(estudante[i].faltas < 22 && media >= 7)
                    printf("\nNome: %s\nMatricula: %i \nFrequênica: %i \nMedia: %.2f\n\n", estudante[i].nome, estudante[i].matricula, estudante[i].faltas,media);
            }
        }

    }

}
int len(struct cadastro estudante[]){
    int contador = 0;
    
    for(int i = 0; i < MAX; i++){
        if(estudante[i].matricula != 0){
            contador++;
        }
    }
    
    return contador;
}
//Função que transfere todos os dados de um aluno para outro aluno
void trocaTroca(struct cadastro vetor[], int len1, int len2){
    int aux;
    float faux;
    char caux[200];
    
    aux = vetor[len2].matricula;
    vetor[len2].matricula = vetor[len1].matricula;
    vetor[len1].matricula = aux;
    
    strcpy(caux, vetor[len2].nome);
    strcpy(vetor[len2].nome, vetor[len1].nome);
    strcpy(vetor[len1].nome, caux);
    
    for(int i = 0; i < 4; i++){
        faux = vetor[len2].notas[i];
        vetor[len2].notas[i] = vetor[len1].notas[i];
        vetor[len1].notas[i] = faux;
    }
    aux = vetor[len2].faltas;
    vetor[len2].faltas = vetor[len1].faltas;
    vetor[len1].faltas = aux;
    
    aux = vetor[len2].codigoTurma;
    vetor[len2].codigoTurma =vetor[len1].codigoTurma;
    vetor[len1].codigoTurma = aux;
    
}

//Função que ordena as matriculas cadastradas no vetor
void borbulharMatricula(struct cadastro vetor[], int len){
    
    for(int i = len; i > 0; i--){
        for(int j = 1; j <= i; j++){
            if(vetor[ j-1].matricula > vetor[j].matricula){
                trocaTroca(vetor, (j-1), j);
            }
        }
    }
}

//Função que ordena os nomes dos alunos em ordem alfabetica
void borbulharNome(struct cadastro vetor[], int len){
    int valor;
    
    for(int i = len; i > 0; i--){
        for(int j = 1; j <= i; j++){
            valor = strcmp(vetor[j-1].nome, vetor[j].nome);
            if(valor > 0){
                trocaTroca(vetor, (j-1), j);
            }
        }
    }
}

//Função que faz um rank das medias dos alunos
void borbulharMedia(struct cadastro vetor[], int len){
    
    for(int i = len; i > 0; i--){
        for(int j = 1; j <= i; j++){
             if(mediaAluno(vetor, j-1) < mediaAluno(vetor, j)){
                trocaTroca(vetor, (j-1), j);
            }
        }
    }
}
//Função que faz uma ordenação pela menor quantidade de faltas.
void borbulharFalta(struct cadastro vetor[], int len){
    
    for(int i = len ;i > 0; i--){
        for(int j = 1; j <= i; j++){
            if(vetor[ j-1].faltas > vetor[j].faltas){
                trocaTroca(vetor, (j-1), j);
            }
        }
    }
}
//Pelo PDF apresentado pelo professor constatamos a necessidade de uma função geral paraa a organização dos dados.

void orgoniza(struct cadastro estudante[]){
    int opcao, tamanho;
    
    tamanho = len(estudante);
    
    printf("1 - ordenar por matricula\n");
    printf("2 - ordenar por nome\n");
    printf("3 - ordenar por media\n");
    printf("4 - ordenar por falta\n\n");
    
    printf("Digite qual opcao deseja: \n");
    scanf("%i", &opcao);
    
    // Menu para o usuario desejar a modalidade de ordenação.

    switch(opcao){
        case 1:
            borbulharMatricula(estudante, tamanho-1);
        break;
        case 2:
            borbulharNome(estudante, tamanho-1);
        break;
        case 3:
            borbulharMedia(estudante, tamanho-1);
        break;
        case 4:
             borbulharFalta(estudante, tamanho-1);
        break;
        
        default:
             printf("\nO valor Digitado não é reconhecido pelo sistema, tente novamente. \n\n");
    }
}
void lerArquivo(struct cadastro estudante[]){
	FILE *cadastramento;
	int i = 0;
	cadastramento = fopen("projeto.txt","r");
	if(cadastramento == NULL)
	  printf("Erro! Não foi possivel abrir op arquivo.\n");
	else{
		while(fscanf(cadastramento,"%i %f %f %f %f %s %i %i",&estudante[i].matricula, &estudante[i].notas[0],&estudante[i].notas[1],&estudante[i].notas[2],&estudante[i].notas[3],estudante[i].nome,&estudante[i].codigoTurma,&estudante[i].faltas)!= EOF){
		
      i++;
	}
		
}
	fclose(cadastramento);
}
void escreverAluno(struct cadastro estudante[]){
	 FILE *cadastramento;
	 int tan;
     cadastramento = fopen("projeto.txt", "w");

	tan = len(estudante);
    
    for(int i = 0; i < tan; i++){
        fprintf(cadastramento,"%i %f %f %f %f %s %i %i\n", estudante[i].matricula, estudante[i].notas[0], estudante[i].notas[1], estudante[i].notas[2], estudante[i].notas[3], estudante[i].nome, estudante[i].codigoTurma, estudante[i].faltas);
	}
    fclose(cadastramento);
}