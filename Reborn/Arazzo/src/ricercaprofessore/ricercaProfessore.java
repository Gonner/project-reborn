package ricercaprofessore;


import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Vector;
import java.util.Map.Entry;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ricercaProfessore {

//per far funzionare il codice si e' scaricato i jar da https://archive.apache.org/dist/poi/release/bin/ versione 3.9
	
	public ricercaProfessore() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
	
	//il metodo ritorna un vector 
	public  Vector<Professore> ricerca() throws IOException {
		
		
		
        String excelFilePath = "/orario_professori.xlsx";			//path per il nome del file
        FileInputStream inputStream = null;  //TODO mettere come oggetto della classe
        try {
			inputStream = new FileInputStream(new File(getClass().getResource(excelFilePath).toURI()));
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        Workbook workbook = new XSSFWorkbook(inputStream);		//inizializzazione per lettura e/o scrittura su file excel
        Sheet firstSheet = workbook.getSheetAt(0);				
        
        Vector<Professore> vettoreProfessori = new Vector<Professore>(); // vettore che ritorna tutti i professori
        
        int contatoreRiga = 2;			//tengo traccia delle righe con un contatore-> parte dalla riga 2 che corrisponde al primo nome
        
        while (contatoreRiga<190) {		//avvio lettura riga*cella tramite un contatore -> da modificare se cambia la lunghezza del file excel
       
            int contatoreOrario = 2;		//contatore per tenere traccia del giorno e l'ora scolastica della giornata IN FONDO SCHEMA
            
            Professore tempProfessore = new Professore();	//creo professore temporaneo per poi essere inserito nel vettore dei professori
            String nomeProfessore = firstSheet.getRow(contatoreRiga).getCell(1).getStringCellValue().trim(); //prelevo il nome del professore

            LinkedHashMap<String,Vector<String>> mappaProfessore = new LinkedHashMap<String, Vector<String>>();	//mappa temporanea per gli orari per giorno che che andr� a Professore
    			Vector<String> temporaneo = new Vector<String>(); // vettore temporaneo per immagazzinare gli orari da mettere nella mappa


            while (contatoreOrario<61) {	//contatore per scorrere tutte le celle -> da modificare in caso di cambiamenti nella struttura degli orari durante i giorni

            				            			                
            	    String ora = firstSheet.getRow(contatoreRiga).getCell(contatoreOrario).getStringCellValue().trim(); //prevelo la classe in ora su cui si posiziona il contatore
            	    if(ora.isEmpty())
            	    	temporaneo.add("");		//controllo se stringa vuota inserisce un campo vuoto
            	    else temporaneo.add(ora);
            	                	    
            	    
            	    if(contatoreOrario == 11){					//controllo a salti in fondo schema
            				mappaProfessore.put("lunedi", temporaneo);temporaneo=new Vector();}
            		
            		else if(contatoreOrario == 22){
            				mappaProfessore.put("martedi", temporaneo);temporaneo=new Vector();}
            		
            		else if(contatoreOrario == 33){
            				mappaProfessore.put("mercoledi", temporaneo);temporaneo=new Vector();}
            		
            		else if(contatoreOrario == 44){
            				mappaProfessore.put("giovedi", temporaneo);temporaneo=new Vector();}
            		
            		else if(contatoreOrario == 55){
            				mappaProfessore.put("venerdi", temporaneo);temporaneo=new Vector();}
            		
            		else if(contatoreOrario == 60){mappaProfessore.put("sabato", temporaneo);temporaneo=new Vector();break;}
            		
        			contatoreOrario++;

            		

            		
            		
            			
            }
            
            
            tempProfessore.setNome(nomeProfessore);		//imposto nome, metto la sua mappa e inserisco professore nel vettore dei professori
            tempProfessore.setMappa(mappaProfessore);
            vettoreProfessori.add(tempProfessore);
            contatoreRiga++;
        }
        
        inputStream.close();
		return vettoreProfessori;
    }

	

}


//in caso di modifiche sarà necessario andare a modificare i contatori (contatoreRiga,contatoreGiorno)



/* per tenere traccia del giorno e allo stesso tempo dell'orario ho posto un indicatore per trovare il giorno
 * 
 * lunedì 		-> 2 fino a 11
 * martedì		-> 12 fino a 22
 * mercoledì		-> 23 fino a 33
 * giovedì		-> 34 fino a 44
 * venerdì		-> 45 fino a 55
 * sabato		-> 56 fino alla sua ultima ora
 * 
 * facendo così ho la possibilità di sapere in che giorno mi trovo e allo stesso tempo ricercare la cella della rispettiva ora del professore
 * 
 * 
 * 
 * la mappa delle ore del professore è strutturata con:
 * 												chiave->giorno della settimana(lunedì,martedì,ecc..)
 * 												valore->vettore con all'interno le varie classi,in questo caso con la posizione
 * 												nel vettore si determina a che ora è inserita quella classe
 * 
 * 
 * ho usato le LinkedHashMap rispetto alle HashMap perchè le HM in qualche modo moficano la posizione di inserimento della chiave
 * le LinkedHashMap invece lasciano inalterato la gerarchia di inserimento, ovviamente l'inserimento è in coda
*/
