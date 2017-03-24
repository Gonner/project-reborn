package ricevimentoProfessore;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Professori {
	
	  
	 private String excelFilePath ;
	 private  FileInputStream inputStream ;
	 private  Workbook workbook;
	 private  Sheet firstSheet ;
	 private  Iterator<Row> iterator;
	 private Set <String> professori;
	 
	 public Professori() throws IOException{
		 excelFilePath = "/orari_ricevimenti.xlsx";
		 try {
				inputStream = new FileInputStream(new File(getClass().getResource(excelFilePath).toURI()));
			} catch (URISyntaxException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	     workbook = new XSSFWorkbook(inputStream);
	     firstSheet = workbook.getSheetAt(0);
	     iterator = firstSheet.iterator();
	     
	     professori = new TreeSet <String>(); 
	     
	     while (iterator.hasNext()) {
             Row nextRow = iterator.next();
             Iterator<Cell> cellIterator = nextRow.cellIterator();
              
             while (cellIterator.hasNext()) {
                 Cell cell = cellIterator.next();
           
                 switch (cell.getCellType()) {
                    case Cell.CELL_TYPE_STRING:
                    	 String prof = cell.getRow().getCell(1).getStringCellValue();
                    if(! professori.contains(prof)){
                    	professori.add(prof);
                    }
                     
                         break;
                     case Cell.CELL_TYPE_BOOLEAN:break;
                     case Cell.CELL_TYPE_NUMERIC:break;
                 }
               //  System.out.print(" - ");
             }
             
         }
          
    	 professori.remove("DOCENTI");
         inputStream.close();
	 }
	 
	 public TreeSet <String> getProfessori(){
		 return (TreeSet<String>) this.professori;

		 
	 }
}
