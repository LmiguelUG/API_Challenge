# ***************************************************************************************************
# ********** Notas: 1.- Se decomprime en el directorio de trabajo actual ****************************
# **********        2.- Se crea una archivo que cintiene la indexación en el directorio actual ******
# ***************************************************************************************************
import os, sys, re, zipfile, pathlib, io


path_to_zip   = os.path.dirname(os.path.abspath(__file__)) + '\enron'
dict_01       = {}
stopwords     = ["able","about","above","abroad","according","accordingly","apr","fre","apt","","across","actually","adj","after","afterwards","again","against","ago","ahead","ain't","all","allow","allows","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","a's","aside","ask","asking","associated","at","available","away","awfully","back","backward","backwards","be","became","because","become","becomes","becoming","been","before","beforehand","begin","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","came","can","cannot","cant","can't","caption","cause","causes","certain","certainly","changes","clearly","c'mon","co","co.","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","c's","currently","dare","daren't","definitely","described","despite","did","didn't","different","directly","do","does","doesn't","doing","done","don't","down","downwards","during","each","edu","eg","eight","eighty","either","else","elsewhere","end","ending","enough","entirely","especially","et","etc","even","ever","evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","fairly","far","farther","few","fewer","fifth","first","five","followed","following","follows","for","forever","former","formerly","forth","forward","found","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","had","hadn't","half","happens","hardly","has","hasn't","have","haven't","having","he","he'd","he'll","hello","help","hence","her","here","hereafter","hereby","herein","here's","hereupon","hers","herself","he's","hi","him","himself","his","hither","hopefully","how","howbeit","however","hundred","i'd","ie","if","ignored","i'll","i'm","immediate","in","inasmuch","inc","inc.","indeed","indicate","indicated","indicates","inner","inside","insofar","instead","into","inward","is","isn't","it","it'd","it'll","its","it's","itself","i've","just","k","keep","keeps","kept","know","known","knows","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","likewise","little","look","looking","looks","low","lower","ltd","made","mainly","make","makes","many","may","maybe","mayn't","mac","tgts","me","mean","meantime","meanwhile","merely","might","mightn't","mine","minus","miss","more","moreover","most","mostly","mr","mrs","much","must","mustn't","my","myself","name","namely","nd","near","nearly","necessary","need","needn't","needs","neither","never","neverf","neverless","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","no-one","nor","normally","not","nothing","notwithstanding","novel","now","nowhere","messageid","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","one's","only","onto","opposite","or","other","others","otherwise","ought","oughtn't","our","ours","ourselves","out","os","outside","over","overall","own","particular","particularly","past","per","perhaps","placed","please","plus","possible","presumably","probably","provided","provides","que","quite","qv","rather","rd","re","really","reasonably","recent","recently","regarding","regardless","regards","relatively","respectively","right","round","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","since","six","so","some","somebody","someday","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that's","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","there'd","therefore","therein","there'll","there're","theres","there's","thereupon","there've","these","they","they'd","they'll","they're","they've","thing","things","think","third","thirty","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","till","to","together","too","took","toward","towards","tried","tries","truly","try","trying","t's","twice","two","un","under","underneath","undoing","unfortunately","unless","unlike","unlikely","until","unto","up","upon","upwards","us","use","used","useful","uses","using","usually","v","value","various","versus","very","via","viz","vs","want","wants","was","wasn't","way","we","we'd","welcome","well","we'll","went","were","we're","weren't","we've","what","whatever","what'll","what's","what've","when","whence","whenever","where","whereafter","whereas","whereby","wherein","where's","whereupon","wherever","whether","which","whichever","while","whilst","whither","who","who'd","whoever","whole","who'll","whom","whomever","who's","whose","why","will","willing","wish","with","within","without","wonder","won't","would","wouldn't","yes","yet","you","you'd","you'll","your","you're","yours","yourself","yourselves","you've","zero","a","how's","i","when's","why's","b","c","d","e","f","g","h","j","l","m","n","o","p","q","r","s","t","u","uucp","w","x","y","z","I","www","amount","bill","bottom","call","computer","con","couldnt","cry","de","describe","detail","due","eleven","empty","fifteen","fifty","fill","find","fire","forty","front","full","give","hasnt","herse","himse","interest","itse”","mill","move","myse”","part","put","show","side","sincere","sixty","system","ten","thick","thin","top","twelve","twenty","abst","accordance","act","added","adopted","affected","affecting","affects","ah","announce","anymore","apparently","approximately","aren","arent","arise","auth","beginning","beginnings","begins","biol","briefly","ca","date","ed","effect","et-al","ff","fix","gave","giving","heres","hes","hid","home","id","im","immediately","importance","important","index","information","invention","itd","keys","kg","km","largely","lets","line","'ll","means","mg","million","ml","mug","na","nay","necessarily","nos","noted","obtain","obtained","omitted","ord","owing","page","pages","poorly","possibly","potentially","pp","predominantly","present","previously","primarily","promptly","proud","quickly","ran","readily","ref","refs","related","research","resulted","resulting","results","run","sec","section","shed","shes","showed","shown","showns","shows","significant","significantly","similar","similarly","slightly","somethan","specifically","state","states","stop","strongly","substantially","successfully","sufficiently","suggest","thered","thereof","therere","thereto","theyd","theyre","thou","thoughh","thousand","throug","til","tip","ts","ups","usefully","usefulness","'ve","vol","vols","wed","whats","wheres","whim","whod","whos","widely","words","world","youd","youre"]
write_path    = os.path.dirname(os.path.abspath(__file__))+ '\indexing.txt'



# ***********************************************************************************
# ********** Función para capturar solicitudes hechas al usuario ********************
# ***********************************************************************************
def interaction():
    print('\n--------------------------------------------------------------------------------------')
    print('Next you must indicate whether the file type\n\t1.- It is compressed (.zip)\n\t2.- It is a directory')
    option = input('\nPlease indicate an option, 1 or 2  ... ')

    if option == '1':
        print('\n\n--------------------------------------------------------------------------------------')
        zip_path = input("\nEnter the path of the .zip file, example: C:\\Users\\user1\download\enron.zip ...  ")
        
        print('Unzipping the .zip, please wait ...')
        decompress_file(zip_path)
        
        print('successful unzipping, applying inverted indices, please wait ...')
        principal(path_to_zip, dict_01)

    elif option == '2':
        print('\n--------------------------------------------------------------------------------------')
        folder_path = input('Enter the path of the folder, example: C:\\Users\\user1\download\enron  ...  ')
        
        print('applying inverted indices, please wait ...')
        principal(folder_path, dict_01)
    
    else:
        option = input('\nIncorrect option, do you want to try again? [Y/N]      ')
        # Llamdo recursivo de la función si el usuario decide interntar nuevamente
        if option == 'Y' or option == 'y':
            interaction()




# ***********************************************************************************
# ********** Función  donde se hara el llamado inicial del programa *****************
# ***********************************************************************************
def principal(path_to_zip,dict_01):
    
    # En el Llamado de la función 'decompress_file'
    #   1.- Extrae todos los directorios/archivos del comprimido .zip en la ruta especificada en el parametro
    # decompress_file (zip_path, path_to_zip)

    # En el Llamado de la función 'browse_directories'
    #   1.- Recorren todos las carpetas hasta llegar a un archivo
    #   2.- Lee cada linea de cada archivo (la normaliza, limpia de caracteres especiales conservando correos existentes: ejemplo: luismiguel123@example.com)
    #   3.- Aplica 'indices invertidos' a cada palabra de cada linea leida
    browse_directories(path_to_zip, dict_01) 
    
    # En el Llamado de la función 'write_file'
    #   1.- Escribe en un archivo 'indexing.txt' el resultado de aplicar 'indices invertidos' en el llamado de la función anterior
    write_file()

    # Petición a usuario
    
    accept = 'y'

    # En el Llamado de la función retriever
    #   1.- Hace una busqueda de la palabra obtenida del usuario en el archivo creado en el llamado de la función 'write_file'
    #   2.- Muestra en consola el resultado de la busqueda
    while (accept == 'y'):
        print('\n--------------------------------------------------------------------------------------')
        word = input('Enter the word you want to search   ')
        word = word.lower()
        retriever(word)
        accept = input('\nyou want to do a new search ? [Y / N] ...  ')
        accept = accept.lower()




# ***********************************************************************************
# ********** Descomprimir archivo .zip en una ruta especificada *********************
# ***********************************************************************************
def decompress_file (zip_path):

    zip_file = zipfile.ZipFile(zip_path, "r")
    try:
        zip_file.extractall( path = path_to_zip)
    except: 
        pass

    zip_file.close()



# ***********************************************************************************
# ********** Recorre los directorios ************************************************
# ***********************************************************************************
def browse_directories (path_to_zip,dict_01):

    if os.path.isdir(path_to_zip):
        folder_content  = os.listdir(path_to_zip)
        cant_elements   = len(folder_content) - 1 
        while(cant_elements >= 0): 
            if folder_content and folder_content[cant_elements] != '__MACOSX':        
                path_aux = path_to_zip + '\\' + folder_content[cant_elements] # Actualiza la ruta de la subcarpeta
                # Si es un directorio recorro los subdirectorios, Si es un archivo leo el archivo
                if (os.path.isdir(path_aux)):     
                    browse_directories(path_aux, dict_01) # Llamado recursivo de la función para recorrer los directorios
                if (os.path.isfile(path_aux)):
                    dict_01 = reading_file(path_aux, dict_01) # Llamado de la función para lectura del archivo  
                    
            cant_elements = cant_elements - 1
    else:
        option = input('invalid directory, do you want to try again? [Y/N]      ')
        # Llamdo recursivo de la función si el usuario decide interntar nuevamente
        if option == 'Y' or option == 'y':
            interaction()



# ***********************************************************************************
# ********** Lectura del archivo ****************************************************
# ***********************************************************************************
def reading_file (file_path, dict_01):
    open_file = open(file_path)
    if open_file:
       dict_01 = reading_line(open_file, file_path, dict_01) # Llamado de la función para lectura de lineas de archivo

    else:
        return 'Problems opening the file.'
    
    return dict_01



# ***********************************************************************************
# ******* Normalización de la linea (todo en minusculas) ****************************
# ***********************************************************************************
def normalize_line(line):
    
    normalized_line = ''
    for word in line:
        word = word.lower()
        normalized_line = normalized_line + word
    return normalized_line



# ***********************************************************************************
# ********** Varificación de si una palabra es un correo electronico ****************
# ***********************************************************************************
def is_email(word):
    # return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', word)
    return re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_'{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", word)



# ***********************************************************************************s
# ********** Verificar si palabra es una palabra vacia (stop word) ******************
# ***********************************************************************************
def is_stop_words(word):
    for stop_word in stopwords:
        if word == stop_word:
            return True
    return False


# ***********************************************************************************
# ********** Limpia la linea de caracteres especiales, en dos etapas ****************
# ***********************************************************************************
def clear_word_1th(word):
    
    characters = "<,>?;"
    for x in range(len(characters)):
        word = (word.replace(characters[x]," "))
    return word



def clear_word_2th(word):
    return (re.sub(r"[^a-zA-Z]","", word))



# ***********************************************************************************
# ********* verificación de existencia del nuevo elemento en una diccionario ********
# ***********************************************************************************
def is_element(new_element, dictionary_aux):
    
    for A in dictionary_aux:
        if A == new_element:
            return True
    return False



# ***********************************************************************************
# ***** Optimiza la lista de coincidencias(no repetidas, no diccionarios anidados) **
# ***********************************************************************************
def opentimize_list(dictionary_01, new_element):
    
    dictionary_aux = []
    for element in dictionary_01:
        if isinstance(element, list):
            for A in element:
                dictionary_aux.append(A)
        else:
            dictionary_aux.append(element)

        if not is_element(new_element, dictionary_aux): 
            dictionary_aux.append(new_element)    
    return dictionary_aux



# ***********************************************************************************
# ********** Indexación de cada palabara de los archivos de la carpeta **************
# ***********************************************************************************
def indexing (path_file, words, dict_01):

    dictionary_01 = []
    for word in words: 
        if not word in dict_01:
            dict_01[word] = path_file           
        else:
            dictionary_01 = []
            dictionary_01.append(dict_01[word])
            new_list = opentimize_list(dictionary_01, path_file) # Llamda de la función para optimizar una lista correcta de rutas con coincidencias de la palabra
            dict_01[word] = new_list
    return dict_01

def delete_spaces(word):
    pass


# ***********************************************************************************
# ********* Lectura de lineas de un archivo definido por la ruta ********************
# ***********************************************************************************
def reading_line(open_file, file_path, dict_01):

    words = []
    line = open_file.readline()     # Lectura de la primera linea
    while line != '': 

        normalized_line = normalize_line(line)
        normalized_line_split = normalized_line.split()
        for word in normalized_line_split:
            word_1th = clear_word_1th(word)
            # print(f'word_1th    {word_1th}')

            if word_1th:           
                if(is_email(word_1th)):
                    words.append(word_1th)
                else:
                    word_2th = clear_word_2th(word_1th)
                    # print(f'word_2th    {word_2th}')
                    if(len(word_2th) > 0 and is_stop_words(word_2th) == False):
                        words.append(word_2th)

        line = open_file.readline() # Actualiza valor de linea leyendo la linea siguiente
    dict_01 = indexing(file_path, words, dict_01)
    return dict_01

 

# ***********************************************************************************
# ********* Escritura de la indexación en un archivo .txt ***************************
# ***********************************************************************************
def  write_file():
    
    open_file = open(write_path, "w")
    if open_file:
        for key in dict_01:
            open_file.write(f'{key}=>{dict_01[key]}\n')
        open_file.close()
    else:
        print('error abriendo archivo de escritura')



# ***********************************************************************************
# ********* Muestra en pantalla los resultados de coincidencia con la bisqueda ******
# ***********************************************************************************
def mostrar(list_coincidences):
    for coincidence in list_coincidences:
        characters = "]["
        for x in range(len(characters)):
            coincidence = coincidence.replace(characters[x],"")
        print(coincidence)   



# ***********************************************************************************
# ********* Obtiene la linea que contenga la palabra buscada ************************
# ***********************************************************************************
def retriever(word):

    file_open = open(write_path, "r")
    line = file_open.readline()     # Lectura de primera linea
    while line != '':
        line_split     = line.split('=>')
        count_splt = len(line_split)
        if(count_splt >= 1):
            if line_split[0] == word:
                line_split_2 = line_split[1].split(', ')
                mostrar(line_split_2)
                
        line = file_open.readline() # Lectura de linea siguiente    
    return dict_01


interaction()

