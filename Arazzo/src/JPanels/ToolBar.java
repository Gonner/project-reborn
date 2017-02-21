package JPanels;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import java.awt.SystemColor;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;

import Global.GlobalVar;
import java.awt.Color;
import javax.swing.JLabel;

public class ToolBar extends JPanel {

	/**
	 * Creo il JPanel che andra' a gestire i movimenti per tornare alla pagina precendente o successiva , questa classe utilizza lo Stack e la StackPosition che si trovano nella classe GlobalVar.
	 *
	 * @see GlobalVar
	 */
	public ToolBar() {
		setBackground(SystemColor.window);

		this.setLayout(null);
		this.setBounds(0, 0, 1280, 40);

		
		final JButton left = new JButton("");
		left.setBorderPainted(false);
		left.setContentAreaFilled(false);
		left.setIcon(new ImageIcon(GlobalVar.img_left_arrow));
		left.setBounds(10, 5, 30, 30);
		add(left);
		
		final JButton right = new JButton("");
		right.setBorderPainted(false);
		right.setContentAreaFilled(false); 
		right.setIcon(new ImageIcon(GlobalVar.img_right_arrow));
		right.setBounds(50, 5, 30, 30);
		add(right);
		
		//base per non far passare il click oltre la toolbar e di conseguenza cliccare altre cose sotto di essa
		JButton base = new JButton("");
		base.setBorderPainted(false);
		base.setContentAreaFilled(false); 
		base.setBounds(0, 0, 1280, 40);
		add(base);
		
		
		left.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent arg0) {
				
			
				left.setIcon(new ImageIcon(GlobalVar.img_left_arrow_pressed));
				
			
				System.out.println("Bottone back premuto");
	
			}
			public void mouseReleased(MouseEvent arg0) {
				
				
				left.setIcon(new ImageIcon(GlobalVar.img_left_arrow));
				if(GlobalVar.StackPosition  > 0)  // se voglio tornare indietro e non vado in underflow
				{
					GlobalVar.StackPosition--; // decremento la posizione attuale in cui mi trovo
					
					GlobalVar.frame.getContentPane().remove(2); // rimuovo il Jpanel che sta nell'indice 2 del frame
					GlobalVar.frame.getContentPane().add(GlobalVar.Stack.get(GlobalVar.StackPosition),2); // setto il Jpanel che e' stato aperto precedentemente
					GlobalVar.frame.repaint();
					GlobalVar.frame.getContentPane().repaint(); // aggiorno la grafica
					
					if(GlobalVar.StackPosition == 0) // se mi trovo alla schermata principale , ovvero di scelta fra ospite e interno
					{
						GlobalVar.menu.setVisible(false); //rendo invisibile la navigationMenu
						GlobalVar.toolbar.setVisible(false); // rendo invisibile la toolbar
					}
				}
				
				
			}
		});
		
		
		right.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent arg0) {
				
				right.setIcon(new ImageIcon(GlobalVar.img_right_arrow_pressed));
			
				System.out.println("Bottone right premuto");
	
			}
			public void mouseReleased(MouseEvent arg0) {
				
				
				right.setIcon(new ImageIcon(GlobalVar.img_right_arrow));
				
				// descrizione dei comandi sono le stesse del bottone 'left'
				if((GlobalVar.StackPosition + 1)< GlobalVar.Stack.size())
				{
					GlobalVar.StackPosition++;
					
					GlobalVar.frame.getContentPane().remove(2);
					GlobalVar.frame.getContentPane().add(GlobalVar.Stack.get(GlobalVar.StackPosition),2);
					GlobalVar.frame.repaint();
					GlobalVar.frame.getContentPane().repaint();
					
					if(GlobalVar.StackPosition == 1) // se mi trovo in posizione successiva a 0(scelta ospite o interno) ovvero 1 , devo attivare il NavigationMenu e la toolbar in modo che siano visibili anche successivamente
					{
						GlobalVar.menu.setVisible(true);
						GlobalVar.toolbar.setVisible(true);
					}
					
				}
				
			}
		});
		
		

	}
}
