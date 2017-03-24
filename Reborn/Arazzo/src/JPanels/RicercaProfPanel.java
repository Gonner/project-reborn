package JPanels;

import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.IOException;
import java.util.Iterator;
import java.util.Set;
import java.util.Vector;

import javax.swing.JPanel;

import ricercaprofessore.GestioneProfessori;
import ricercaprofessore.Professore;
import ricevimentoProfessore.FindOrarioRicevimentoProfessore;
import ricevimentoProfessore.Professori;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

import Global.GlobalVar;
import customObject.MyComboBoxRenderer;

import java.awt.Color;
import java.awt.Font;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class RicercaProfPanel extends JPanel {

	
	int ora=0;
	String giorno="lunedi";
	String prof="aldi";
	
	private JTextField textField;
	/**
	 * Create the panel.
	 */
	public RicercaProfPanel() {
		setOpaque(false); //sfondo trasparente del panel per permettere la visione dello sfondo del jframe

		this.setLayout(null);
		this.setBounds(0, 0, 1280, 1024);
		
		final GestioneProfessori gestione = new GestioneProfessori();
		gestione.caricaProfessori();
		Vector<Professore> tmp = null;
		tmp = gestione.getProfessori();
		
		if(tmp == null)
			System.out.print("nessun porf trovato , controllare nome file xls");
	
			String[] ore = new String[17];  
			int j=0;
			
			for(int i=8;i<24;i++){
				ore[j]= i+":00 - "+(i+1)+":00";
				j++;
			}
		
			String[] giorni = new String[]{"Lunedi","Martedi","Mercoledi","Giovedi","Venerdi","Sabato"};
			
			String[] professori = new String[190];  // stringa che conterra' tutti i professori

			for(int i=0;i<184;i++){
				System.out.println(tmp.get(i));
				professori[i] = tmp.get(i).toString();
			}
			
			
			textField = new JTextField();
			textField.setBackground(Color.WHITE);
			textField.setEditable(false);
			textField.setHorizontalAlignment(SwingConstants.CENTER);
			textField.setFont(new Font("Oswald", Font.PLAIN, 35));
			textField.setBorder(null);
			textField.setOpaque(false);
			textField.setBounds(329, 847, 600, 40);
			add(textField);
			textField.setColumns(10);
			
			final JComboBox OrecomboBox = new JComboBox(ore);
			OrecomboBox.setBounds(788, 300, 200, 30);
			OrecomboBox.setFont(new Font("Oswald", Font.BOLD, 22));
			OrecomboBox.addItemListener(new ItemListener() {
			      public void itemStateChanged(ItemEvent e) {
			    	
						ora = OrecomboBox.getSelectedIndex();
						String tmp = gestione.cercaProfessoreInOra(prof, ora+1, giorno);
						if(tmp.equals("") || tmp.equals(" "))
							textField.setText("non effettua lezioni in questa ora");
						else
							textField.setText(tmp);
			        }
			      });
			add(OrecomboBox);
			
			final JComboBox GiornicomboBox = new JComboBox(giorni);
			GiornicomboBox.setBounds(533, 300, 200, 30);
			GiornicomboBox.setFont(new Font("Oswald", Font.BOLD, 22));
			GiornicomboBox.addItemListener(new ItemListener() {
			      public void itemStateChanged(ItemEvent e) {
			    	  
			    	
			    	  giorno = GiornicomboBox.getSelectedItem().toString().toLowerCase();
			    	  String tmp = gestione.cercaProfessoreInOra(prof, ora+1, giorno);
						if(tmp.equals("") || tmp.equals(" "))
							textField.setText("non effettua lezioni in questa ora");
						else
							textField.setText(tmp);
			        }
			      });
			add(GiornicomboBox);

			
			final JComboBox ProfcomboBox = new JComboBox(professori);
			ProfcomboBox.setBounds(267, 300, 200, 30);
			ProfcomboBox.setFont(new Font("Oswald", Font.BOLD, 22));
			ProfcomboBox.addItemListener(new ItemListener() {
			      public void itemStateChanged(ItemEvent e) {
			    	  
			    	
			    	  prof = ProfcomboBox.getSelectedItem().toString();
			    	  
			    	  	System.out.println(prof);
						System.out.println(ora);
						System.out.println(giorno);
						String tmp = gestione.cercaProfessoreInOra(prof, ora+1, giorno);
						if(tmp.equals("") || tmp.equals(" "))
							textField.setText("non effettua lezioni in questa ora");
						else
							textField.setText(tmp);
			        }
			      });
			add(ProfcomboBox);
			
			
			
			JLabel background = new JLabel("");
			background.setIcon(new ImageIcon(GlobalVar.img_ricercaprof_panel));
			background.setBounds(0, 0, 1280, 1024);
			add(background);
			
			 String app = gestione.cercaProfessoreInOra(prof, ora+1, giorno);
			if(app.equals("") || app.equals(" "))
				textField.setText("non effettua lezioni in questa ora");
			else
				textField.setText(app);
			
	}
}

