package Global;
import java.awt.Image;
import java.util.Vector;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

import JPanels.NavigationMenu;
import JPanels.OspitiInterniPanel;
import JPanels.TmpPanel;
import JPanels.ToolBar;

/**
 * Classe che contiene tutte le variabili che servono istanziate staticamente come le immagini , in modo da non creare rallentamenti in runtime al costo di aspettare qualche secondo all'avvio del SW,
 * la classe contiene anche delle variabili che sono utili durante la programmazione come il frame o lo stack
 *	
 *	le variabili che iniziano con img_ sono immagini , quelle che iniziano con path_ sono i percorsi delle immagini all'interno del progetto.
 *	
 */

public class GlobalVar {
	
	public static JPanel toolbar;
	public static JPanel menu;
	public static JFrame frame;  // frame principale
	
	public static Image img_btn_ospiti;
	public static Image img_btn_ospiti_pressed;
	public static Image img_btn_interni;
	public static Image img_btn_interni_pressed;
	public static Image img_background;
	public static Image img_left_arrow;   // bottone back toolbar
	public static Image img_right_arrow;  // bottone forward toolbar
	public static Image img_left_arrow_pressed; // btn premuto toolbar
	public static Image img_right_arrow_pressed; // btn premuto toolbar
	public static Image img_close_menu;  // X
	public static Image img_open_menu;  // tre linee
	public static Image img_navigation_menu;
	
	public static String path_btn_ospiti = "/images/btn_ospiti.png";
	public static String path_btn_ospiti_pressed = "/images/btn_ospiti_pressed.png";
	public static String path_btn_interni = "/images/btn_interni.png";
	public static String path_btn_interni_pressed = "/images/btn_interni_pressed.png";
	public static String path_background = "/images/background.png";
	public static String path_left_arrow = "/images/left_arrow.png";
	public static String path_right_arrow = "/images/right_arrow.png";
	public static String path_left_arrow_pressed = "/images/left_arrow_pressed.png";
	public static String path_right_arrow_pressed = "/images/right_arrow_pressed.png";
	public static String path_close_menu = "/images/close_cross.png";
	public static String path_open_menu = "/images/menu_icon.png";
	public static String path_navigation_menu = "/images/navigation_menu.png";
	
	public static int StackPosition=0;
	public static Vector<JPanel> Stack = new Vector<JPanel>(1,1);
	
	public static boolean Ospite = false;   // flag per capire se e' stato selezionato ospite o interno
	public static boolean Interno = false;
	
	
	/**
	 * Costruttore che istanzia le variabili.
	 */
	public GlobalVar()
	{
		
		//istanzio tutte le immagini
		try{
			
			img_btn_interni =ImageIO.read(getClass().getResource(path_btn_interni));
			img_btn_ospiti =ImageIO.read(getClass().getResource(path_btn_ospiti));
			img_btn_ospiti_pressed = ImageIO.read(getClass().getResource(path_btn_ospiti_pressed));
			img_btn_interni_pressed = ImageIO.read(getClass().getResource(path_btn_interni_pressed));
			img_background =  ImageIO.read(getClass().getResource(path_background));
			img_left_arrow = ImageIO.read(getClass().getResource(path_left_arrow));
			img_right_arrow = ImageIO.read(getClass().getResource(path_right_arrow));
			img_left_arrow_pressed = ImageIO.read(getClass().getResource(path_left_arrow_pressed));
			img_right_arrow_pressed = ImageIO.read(getClass().getResource(path_right_arrow_pressed));
			img_close_menu = ImageIO.read(getClass().getResource(path_close_menu));
			img_open_menu = ImageIO.read(getClass().getResource(path_open_menu));
			img_navigation_menu = ImageIO.read(getClass().getResource(path_navigation_menu));
			
			Stack.add(0,new OspitiInterniPanel());
			
		
		}catch(Exception e){
			
			e.printStackTrace();
		}
	
	}
	


}
