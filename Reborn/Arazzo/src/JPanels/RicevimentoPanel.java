package JPanels;

import javax.swing.JPanel;
import javax.swing.JComboBox;

import java.awt.ItemSelectable;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.IOException;
import java.util.Iterator;
import java.util.Set;
import javax.swing.JTextField;

import Global.GlobalVar;
import customObject.MyComboBoxRenderer;
import ricevimentoProfessore.FindOrarioRicevimentoProfessore;
import ricevimentoProfessore.Professori;

import java.awt.Color;
import java.awt.Font;

import javax.swing.DefaultComboBoxModel;
import javax.swing.ImageIcon;

import java.awt.SystemColor;
import java.awt.TextField;

import javax.swing.JLabel;
import javax.swing.SwingConstants;

public class RicevimentoPanel extends JPanel {

	/**
	 * Create the panel.
	 */
	
	int nuProfessori = 189;    //importante!   , dimensione del vettore per immagazzinare i professori
	private JTextField giorno;
	private JTextField orario;
	private FindOrarioRicevimentoProfessore f;
	public RicevimentoPanel() {
		setOpaque(false); //sfondo trasparente del panel per permettere la visione dello sfondo del jframe

		this.setLayout(null);
		this.setBounds(0, 0, 1280, 1024);
		
		 Set <String> tmp = null;
    	 
    	Professori p;
		try {
			p = new Professori();
			tmp =  p.getProfessori(); 
		} catch (IOException e1) {
			
			e1.printStackTrace();
		}
		
		String[] professori = new String[190];  // stringa che conterra' tutti i professori
		int i=0;
		 for (Iterator<String> it = tmp.iterator(); it.hasNext(); ) {
		        String obj = it.next();
		        if(!obj.equals("") && !obj.equals(" ")){
		        	professori[i] = obj;
		        	i++;
		        }
		    }
    	
			 giorno = new JTextField();
			 giorno.setHorizontalAlignment(SwingConstants.CENTER);
			 giorno.setFont(new Font("Oswald", Font.PLAIN, 30));
			 giorno.setBorder(null);
			 giorno.setOpaque(false);
			 giorno.setEditable(false);
			 giorno.setBounds(512, 336, 236, 37);
				add(giorno);
				giorno.setColumns(10);
			
			 orario = new JTextField();
			 orario.setHorizontalAlignment(SwingConstants.CENTER);
			 orario.setFont(new Font("Oswald", Font.PLAIN, 30));
			 orario.setBorder(null);
			 orario.setOpaque(false);
			 orario.setEditable(false);
			 orario.setBounds(780, 336, 236, 37);
				add(orario);
				orario.setColumns(10);
    	
		final JComboBox comboBox = new JComboBox(professori);
		comboBox.setMaximumRowCount(15);
		comboBox.setFont(new Font("Oswald", Font.BOLD, 22));
		comboBox.addItemListener(new ItemListener() {
		      public void itemStateChanged(ItemEvent e) {
		    	  
					try {
						
						f = new FindOrarioRicevimentoProfessore(comboBox.getSelectedItem().toString());
						giorno.setText(f.getGiorno());
						orario.setText(f.getOrario());
						
					} catch (IOException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
		        }
		      });
		comboBox.setBounds(267, 340, 200, 30);
		
		add(comboBox);
		
		JLabel background = new JLabel("");
		background.setIcon(new ImageIcon(GlobalVar.img_ricevimento_panel));
		background.setBounds(0, 0, 1280, 1024);
		add(background);
		
		try {
			f = new FindOrarioRicevimentoProfessore(professori[0]);
			giorno.setText(f.getGiorno());
			orario.setText(f.getOrario());
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

	}
}
