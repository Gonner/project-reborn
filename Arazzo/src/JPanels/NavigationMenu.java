package JPanels;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.JLabel;

import Global.GlobalVar;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.Font;
import javax.swing.JSeparator;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Vector;

import javax.swing.Timer;
import java.awt.SystemColor;

public class NavigationMenu extends JPanel implements ActionListener {
	
	 boolean menu_opened = true;
	 Timer tm = new Timer(5,this);  // timer per animazione
	 int x = 0 , velX = 4;   // coordinate e volicita' per animazione
	 
	/**
	 *  JPanel che gestisce la navigazione dell'utente una volta scelto se essere ospite o interno , le opzioni vengono caricate dinamicamente a seconda della scelta fatta.
	 */
	public NavigationMenu() {
		
		Vector<String> opt_ospite = new Vector<String>(1,1);   //opzioni per ospiti
		Vector<String> opt_interno = new Vector<String>(1,1);  //opzioni per interni
		
			//assegnazione option del menu
		opt_interno.add("Visualizzazione comunicazioni");
		opt_interno.add("Variazioni orario scolastico");
		opt_interno.add("Ricerca professore");
		opt_interno.add("Elenco foto insegnanti");
		opt_interno.add("Planimetria Buzzi");
		
		opt_ospite.add("Presentazione Istituto");
		opt_ospite.add("Tour virtuale 360°");
		opt_ospite.add("Museo");
		
		
		this.setBounds(-390, 40, 446, 994);
		this.setLayout(null);
		this.setOpaque(false);
		
		//label per fare background del JPanel
		JLabel menu = new JLabel("");  
		menu.setBounds(0, 0, 446, 994);
		menu.setIcon(new ImageIcon(GlobalVar.img_navigation_menu));
		this.add(menu);
		
		//TODO fixare problema animazione navigation menu
		tm.start(); // avvio una prima volta l'animazione altrimenti si bugga 
		
		
		
		final JButton btn = new JButton("");   // bottono apri/chiudi menu
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent arg0) {
				
				if(menu_opened){ // se menu aperto
					tm.start();  // avvio animazione
					//setBounds(-390, 40, 446, 994);
					menu_opened=false;
					btn.setIcon(new ImageIcon(GlobalVar.img_close_menu));
				
				}
				else{ // se chiuso
					tm.start(); // avvio animazione
					//setBounds(0, 40, 446, 994);
					menu_opened=true;
					btn.setIcon(new ImageIcon(GlobalVar.img_open_menu));
				}
			}
		});
	
		btn.setBounds(393, 10, 40, 40);  
		btn.setBorderPainted(false);
		btn.setContentAreaFilled(false);
		btn.setIcon(new ImageIcon(GlobalVar.img_open_menu));
		menu.add(btn);
		
		//creazione dinamica dei bottoni all'interno del menu
		if(GlobalVar.Interno==true)
		{
			int pos = 50; //posizione y del bottone
			for(int i=0 ; i< opt_interno.size(); i++){
				menu.add(makeBtn(opt_interno.get(i),pos));

				pos = pos + 55;  // distanza fra una opzione e l'altra
				
				JSeparator separator = new JSeparator();	
				separator.setForeground(SystemColor.controlDkShadow);
				separator.setBounds(10, pos, 350, 1);
				menu.add(separator);
			}
		}
		else if(GlobalVar.Ospite==true)
		{
			int pos = 50; //posizione del bottone
			
			for(int i=0 ; i< opt_ospite.size(); i++){
				menu.add(makeBtn(opt_ospite.get(i),pos));

				pos = pos + 55; // distanza fra una opzione e l'altra
				
				JSeparator separator = new JSeparator();	
				separator.setForeground(SystemColor.controlDkShadow);
				separator.setBounds(10, pos, 360, 1);
				menu.add(separator);
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
 * Azione che viene eseguita quando viene clicckato il bottono per aprire o chiudere o aprire il menu , in modo tale da avviare l'animazione
 * @param arg0 bottone del menu premuto
 */
	public void actionPerformed(ActionEvent arg0) {

		if(menu_opened==true && x >= -390){
		x = x - velX;
		setBounds(x, 40, 446, 994);
				
		}
		else if(menu_opened==false && x <= -4)
		{
			x = x + velX;
			setBounds(x, 40, 446, 994);

		}
		
	}
	
	/**
	 * metodo che restituisce un botton creato con una stringa che definisce l'opzione e la sua posizione nell'asse y dello schermo
	 * @param opt String opzione
	 * @param pos Integer posizione sull'asse Y
	 * @return JButton
	 */
	
	public JButton makeBtn(String opt, Integer pos){
		
		JButton btn = new JButton(opt);
		btn.setBorderPainted(false);
		btn.setFocusPainted(false);
		btn.setContentAreaFilled(false);
		btn.setFont(new Font("Oswald", Font.BOLD, 22));
		btn.setHorizontalAlignment(SwingConstants.CENTER);
		btn.setBounds(10, pos, 360, 50);

		
		
		return btn;
	}
	
}
