from time import sleep

def exit(): 
    print('Ok, saindo...')
    sleep(2)
    print('Programa encerrado!')

def porcentagemPlaylistUX(): 
    while True: 
        var_choice = input('Deseja utilizar o PorcentagemPlaylist Python? [S/N]: ').upper()

        if var_choice == 'S': 
            dict_mus = {'genero_musica': []}
            dict_mus_count = {}
            total_songs = 0
            
            x = 0 
            while x < 4: 
                genre = input(f'Digite um dos seus quatro gêneros de música preferidos ({x+1}/4): ')
                dict_mus['genero_musica'].append(genre)
                count = int(input(f'Quantas músicas de {genre} você possui em sua playlist: '))
                dict_mus_count[genre] = count
                total_songs += count
                x += 1
                
            print("\nPorcentagem de cada gênero na sua playlist:")
            for genre, count in dict_mus_count.items():
                percentage = (count / total_songs) * 100
                print(f"{genre}: {percentage:.2f}%")
                
            break
            
        elif var_choice == 'N': 
            exit()
            break

if __name__ == '__main__': 
    porcentagemPlaylistUX()
