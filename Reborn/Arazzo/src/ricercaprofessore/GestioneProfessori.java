package ricercaprofessore;

import java.io.IOException;
import java.util.Vector;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class GestioneProfessori {
	
	Vector<Professore> professori;


	public GestioneProfessori() {
		super();
		
	}

	public Vector<Professore> getProfessori() {
		return professori;
	}

	public void setProfessori(Professore p) {
		this.professori.addElement(p);
	}
	
	public void caricaProfessori()
	{
		ricercaProfessore ricerca = new ricercaProfessore();
		try
		{
			this.professori = ricerca.ricerca();
		}catch (IOException e) {}
	}
	
	public void stampaTutti()		//stampa tutti i professori con tutti gli orari
	{
		for(int i = 0;i<professori.size();i++)
		{
			System.out.println(professori.elementAt(i).getNome()+"\n");
			
			for(Entry entry : professori.elementAt(i).getMappa().entrySet())
			{
			    String key = (String) entry.getKey();
			    Vector<String> orari = (Vector<String>) entry.getValue();
			   
			    System.out.println(key + ":");
			    
			    for(int k=0;k<orari.size();k++)
			    {
			    		System.out.println((k+1) + "°" + "->" + orari.elementAt(k));
			    }

			    
			}
			
		}System.out.println("\n");
	}
	
	public void stampaProfessore(String nome)		//stampa orario di un professore
	{
		String cercato = nome;
		cercato = cercato.toUpperCase();
		for(int i = 0;i<professori.size();i++)
		{
			if(professori.elementAt(i).getNome().equals(cercato))
			{
				System.out.println(professori.elementAt(i).getNome()+"\n");
				
				for(Entry entry : professori.elementAt(i).getMappa().entrySet())
				{
				    String key = (String) entry.getKey();
				    Vector<String> orari = (Vector<String>) entry.getValue();
				   
				    System.out.println(key + ":");
				    
				    for(int k=0;k<orari.size();k++)
				    {
				    		System.out.println((k+1) + "°" + "->" + orari.elementAt(k));
				    }
	
				    
				}
			}
			
		}
	}
	
	public String cercaProfessoreInOra(String nome,int ora, String giorno) {	//stampa orario professore in un giorno a una determinata
		String cercato = nome.toUpperCase();
		for(int i = 0;i<professori.size();i++)
		{
			if(professori.elementAt(i).getNome().equals(cercato))
			{
				System.out.println(professori.elementAt(i).getNome()+"\n");
				
				for(Entry entry : professori.elementAt(i).getMappa().entrySet())
				{
				    String key = (String) entry.getKey();
				    Vector<String> orari = (Vector<String>) entry.getValue();
				    
				   if(key.equals(giorno))
				   {
					    System.out.println(key+":");
					    try{
					    System.out.println((ora) + "°" + "->" + orari.elementAt(ora-1));  // se da errore di index out of bound vuol dire che non lavora in quelle ore
					    }
					    catch (ArrayIndexOutOfBoundsException e) {
							return " ";
						}
					    return orari.elementAt(ora-1);
				   }
				    
				}
			}
			
		}
		return "";
	}
	
	
	public static void main(String args[])
	{
		GestioneProfessori g = new GestioneProfessori();
		
		g.caricaProfessori();		//inizializza tutti i professori
		
		
		//esempio della terza ricerca
		String cercato = "mocali";
		g.cercaProfessoreInOra("aldi",1,"lunedi");
		
	}
	
	
}
