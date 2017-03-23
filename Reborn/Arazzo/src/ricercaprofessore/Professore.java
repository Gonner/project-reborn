package ricercaprofessore;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.Vector;

public class Professore {
	
	private String nome;
	private LinkedHashMap<String,Vector<String>> mappa;
	
	public Professore()
	{
		
	}
	
	
	public String getNome() {
		return nome;
	}


	public void setNome(String nome) {
		this.nome = nome;
	}


	public HashMap<String, Vector<String>> getMappa() {
		return mappa;
	}


	public void setMappa(LinkedHashMap<String, Vector<String>> professore) {
		this.mappa = professore;
	}


	@Override
	public String toString() {
		return nome.toUpperCase();
	}
	
	
	

}
