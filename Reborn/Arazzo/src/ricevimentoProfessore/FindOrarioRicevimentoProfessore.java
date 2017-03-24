package ricevimentoProfessore;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Iterator;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class FindOrarioRicevimentoProfessore {

	private String excelFilePath;
	private FileInputStream inputStream;
	private Workbook workbook;
	private Sheet firstSheet;
	private Iterator<Row> iterator;
	private String risultato;
	private String giorno; 
	private String orario; 

	public FindOrarioRicevimentoProfessore(String prof) throws IOException {
		 excelFilePath = "/orari_ricevimenti.xlsx" ;
		try {
			inputStream = new FileInputStream(new File(getClass().getResource(excelFilePath).toURI()));
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		workbook = new XSSFWorkbook(inputStream);
		firstSheet = workbook.getSheetAt(0);
		iterator = firstSheet.iterator();

		while (iterator.hasNext()) { // iteratore per le colonne
			Row nextRow = iterator.next();
			Iterator<Cell> cellIterator = nextRow.cellIterator(); // iteratore
																	// per la
																	// riga

			while (cellIterator.hasNext()) {
				Cell cell = cellIterator.next();

				switch (cell.getCellType()) {
				case Cell.CELL_TYPE_STRING:
					trovaRiga(prof, cell);
					break;
				case Cell.CELL_TYPE_BOOLEAN:
					break;
				case Cell.CELL_TYPE_NUMERIC:
					break;
				}
			}

		}

		inputStream.close();

	}

	public void trovaRiga(String professore, Cell cell) {

		if (cell.getStringCellValue().equals(professore)) {
			if (!cell.getRow().getCell(2).getStringCellValue().equals("")){
				giorno = "lunedi";
				orario = cell.getRow().getCell(2).getStringCellValue(); 
				
			}
		
			if (!cell.getRow().getCell(3).getStringCellValue().equals("")){
				giorno = "martedi";
				orario = cell.getRow().getCell(3).getStringCellValue();
			}
				
			if (!cell.getRow().getCell(4).getStringCellValue().equals("")){
				giorno = "mercoledi";
				orario =  cell.getRow().getCell(4).getStringCellValue();
			}
		
			if (!cell.getRow().getCell(5).getStringCellValue().equals("")){
				giorno = "giovedi";
				orario = cell.getRow().getCell(5).getStringCellValue();
			}
			
			if (!cell.getRow().getCell(6).getStringCellValue().equals("")){
				giorno = "venerdi";
				orario =  cell.getRow().getCell(6).getStringCellValue();
			}
			
			if (!cell.getRow().getCell(7).getStringCellValue().equals("")){
				giorno = "sabato";
				orario = cell.getRow().getCell(7).getStringCellValue();
				
			}
				

		}
		
		
	}
	
	public String getRisultato(){
		giorno = giorno.toUpperCase(); 
		String ora = orario.substring(0,7);
		orario= orario.substring(orario.length()-15,orario.length());
		
		risultato = giorno+" "+ora+" "+orario;
		return this.risultato; 
	}

	public String getGiorno() {
		return giorno;
	}


	public String getOrario() {
		orario= orario.substring(orario.length()-15,orario.length());
		return orario;
	}

	
	
	

}
