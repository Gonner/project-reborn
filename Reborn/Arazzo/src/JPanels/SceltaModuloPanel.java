package JPanels;

import java.awt.Color;
import java.awt.Font;
import java.awt.SystemColor;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Vector;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.SwingConstants;

import Global.GlobalVar;

public class SceltaModuloPanel extends JPanel {
	Vector<String> opt_ospite;
	Vector<String> opt_interno; 
	/**
	 * Create the panel.
	 */
	public SceltaModuloPanel() {
		setOpaque(false);
		this.setBounds(0, 0, 1280, 1024);
		setLayout(null);
	
		opt_ospite = new Vector<String>(1,1);   //opzioni per ospiti
		opt_interno = new Vector<String>(1,1);  //opzioni per interni
		
			//assegnazione option del menu
		opt_interno.add("Ricerca professore");
		opt_interno.add("Planimetria Buzzi");
		opt_interno.add("Visualizzazione orario ricevimenti");
		opt_interno.add("Visualizzazione comunicazioni");
		opt_interno.add("Variazioni orario scolastico");
		
		opt_ospite.add("Presentazione Istituto");
		opt_ospite.add("Tour virtuale 360°");
		opt_ospite.add("Museo");

		if(GlobalVar.Interno==true)
		{
			int pos = 150; //posizione y del bottone
			for(int i=0 ; i< opt_interno.size(); i++){
				this.add(makeBtn(opt_interno.get(i),pos));
				
				pos = pos + 155;  // distanza fra una opzione e l'altra
				
			}
		}
		else if(GlobalVar.Ospite==true)
		{
			int pos = 250; //posizione del bottone
			
			for(int i=0 ; i< opt_ospite.size(); i++){
				this.add(makeBtn(opt_ospite.get(i),pos));

				pos = pos + 155; // distanza fra una opzione e l'altra
				
			}
		}
				
				
		
		
		//base per non far passare il click oltre la toolbar e di conseguenza cliccare altre cose sotto di essa
				JButton base = new JButton("");
				base.setBorderPainted(false);
				base.setContentAreaFilled(false); 
				base.setBounds(0, 0, 446, 994);
				add(base);
	}


	
	/**
	 * metodo che restituisce un botton creato con una stringa che definisce l'opzione e la sua posizione nell'asse y dello schermo
	 * @param opt String opzione
	 * @param pos Integer posizione sull'asse Y
	 * @return JButton
	 */
	
	public JButton makeBtn(String opt, final Integer pos){
		
		final JButton btn = new JButton(opt);
		
		btn.setBounds(380, pos, 495, 140);
		btn.setIcon(new ImageIcon(GlobalVar.img_btn_mod));
		btn.setFont(new Font("Oswald", Font.BOLD, 28));
		btn.setForeground(Color.decode("#565656"));
		btn.setVerticalTextPosition(JButton.CENTER);
		btn.setHorizontalTextPosition(JButton.CENTER);
		btn.setBorderPainted(false);
		btn.setFocusPainted(false);
		btn.setContentAreaFilled(false);
	
	
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent arg0) {
				
				btn.setIcon(new ImageIcon(GlobalVar.img_btn_mod_pressed));
				btn.setBounds(380, (pos + 10), 495, 140);
			
				
				
			}
			public void mouseReleased(MouseEvent arg0) {
				
				btn.setBounds(380, pos, 495, 140);
				btn.setIcon(new ImageIcon(GlobalVar.img_btn_mod));
				

				if(GlobalVar.Interno==true)
				{
					if(btn.getText().equals(opt_interno.get(0)))
					{
						JPanel tmp = new RicercaProfPanel();
						
						GoToPanel(tmp);
					}
					else if(btn.getText().equals(opt_interno.get(1)))
					{
						
					}
					else if(btn.getText().equals(opt_interno.get(2)))
					{
						
						JPanel tmp = new RicevimentoPanel();
						
						GoToPanel(tmp);
						
					}
					else if(btn.getText().equals(opt_interno.get(3)))
					{
						
					}
					else if(btn.getText().equals(opt_interno.get(4)))
					{
						
					}
				}
				else if(GlobalVar.Ospite==true)
				{
					if(btn.getText().equals(opt_ospite.get(0)))
					{
						System.out.println("primo");
					}
					else if(btn.getText().equals(opt_ospite.get(1)))
					{
						
					}
					else if(btn.getText().equals(opt_ospite.get(2)))
					{
						
					}
				}
			}
		});
		
		
		return btn;
	}
	
	public void GoToPanel (JPanel tmp){  // da migliorare  ( possibilmente se esiste il jpanel andare direttamente alla posizione dello stack in cui e' istanziato ed eliminare i successivi (forse))
		
		if((GlobalVar.Stack.get(GlobalVar.StackPosition).getClass()).equals(tmp.getClass())) //controlla se si tenta di aprire la stessa finestra
		{
			
			
		}
		else
		{
			GlobalVar.frame.getContentPane().remove(2); // + 2 perche 0  e 1 sono riservati alla toolbar e al menu
			GlobalVar.frame.getContentPane().add(tmp,2);  // imposto nell'indice 2 (dove setto tutte le schermate) il Jpanel che voglio
			
			
			if(GlobalVar.Stack.size() == GlobalVar.StackPosition) 	// se l'indice dello stack non e' istanziato
				GlobalVar.Stack.add(GlobalVar.StackPosition,tmp);    // add jpanel
			else													// altrimenti					
				GlobalVar.Stack.set(GlobalVar.StackPosition,tmp);	// set jpanel
		}
		GlobalVar.frame.repaint();
		GlobalVar.frame.getContentPane().repaint();  // i repaint servono per far si che la grafica si aggiorni , altrimenti diventa tutto glitchato
		
	}

}
