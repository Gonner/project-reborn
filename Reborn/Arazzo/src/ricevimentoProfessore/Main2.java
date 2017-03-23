package ricevimentoProfessore;


import java.io.IOException;
import java.util.Iterator;
import java.util.Set;

 

/**
 * A dirty simple program that reads an Excel file.
 * @author www.codejava.net
 *
 */
/* per leggere il file excelscaricare i file jar dal sito https://archive.apache.org/dist/poi/release/bin/ 
 * SCARICA L'ULTIMA VERSIONE 3.9 */
public class Main2 {
     

   
       

    public static void main(String[] args) throws IOException {
    	
    	 Set <String> vett;
    	 String risultato=null;
    	 
    	Professori p = new Professori();
    	vett =  p.getProfessori(); 
    	
    	
        
        Iterator<String> it = vett.iterator(); 
        while(it.hasNext()){
        	System.out.println(it.next().toString());
        }
        
        
        FindOrarioRicevimentoProfessore f = new FindOrarioRicevimentoProfessore("PANZARELLA F.");
        risultato=f.getRisultato(); 
        System.out.println(risultato);
        
    }
   
 
}
