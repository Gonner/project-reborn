import java.awt.EventQueue;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import Global.GlobalVar;
import JPanels.NavigationMenu;
import JPanels.ToolBar;

/**
 * Classe che gestisce la Finestra con cui si andra' ad interfacciare l'utente
 *
 */

public class MainFrame {

	private static JFrame frame;

	/**
	 * Launch the application.
	 * 
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainFrame window = new MainFrame();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 *  con new GlobalVar() , istanzio nella classe GlobalVar tutte la variabili che mi servono statiche , ad esempio le immagini
	 *  con inizialize() , inizializzo il frame con le sue componenti
	 * @see GlobalVar
	 */
	public MainFrame() {
		
		//istanzio le variabili globali
		new GlobalVar();
		
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 * device , e' variabile utilizzata per trovare le deminsioni dello schermo del device attualmente utilizzato e di conseguenza mettere il frame a tutto schermo
	 * panel, e' variabile di supporto per istanziare la toolbar , il navigationmenu e il jpanel di scelta ospite o interno
	 * background, e' variabile di tipo label , messa a tutto schermo ed utilizzata per creare il background del frame , non e' il metodo ufficiale ma e' comunque efficace 
	 * GlobalVar.Stack , e' variabile di tipo vector in cui tengo conto della path di finestra fatta dall'utente , serve per tornare ad una schermata precedente o successiva gia' aperta
	 * GlobalVar.StackPosition, e' variabile che tiene conto della posizione nello stack , di conseguenza della posizione in cui si trova l'utente
	 *
	 * @return void
	 * @see ToolBar
	 * @see NavigationMenu
	 * @see GlobalVar
	 */
	private void initialize() {
		//prende le informazioni dello screen del device utilizzato
		GraphicsDevice device = GraphicsEnvironment
			    .getLocalGraphicsEnvironment().getDefaultScreenDevice();
		
		
		frame = new JFrame();
		//frame.setExtendedState(JFrame.MAXIMIZED_BOTH); 
		frame.setUndecorated(true);  // nascondo toolbar del sistema operativo
		frame.setSize(1280, 1024);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);  //absolute layout
	
		//setto la toolbar
		JPanel panel = new ToolBar();
		panel.setVisible(false);
		frame.getContentPane().add(panel,0);
		GlobalVar.toolbar = panel;  // salvo la toolbar per farla apparire quando voglio
		
		panel = new NavigationMenu();
		panel.setVisible(false);
		frame.getContentPane().add(panel,1);
		GlobalVar.menu = panel; // salvo il navigation menu , casomai dovesse servire

		//settaggio Jpanel
		panel = GlobalVar.Stack.get(GlobalVar.StackPosition);   // prendo dalla classe globalVar del package Global lo stack e la pos attuale dello stack
		frame.getContentPane().add(panel,2);  //addo il panel al frame
		
	
		// frame background
		JLabel background = new JLabel("");
		background.setIcon(new ImageIcon(GlobalVar.img_background));
		background.setBounds(0, 0, 1280, 1024);
		frame.getContentPane().add(background);
		
		GlobalVar.frame = frame;  // salvo frame per apportare modifiche al frame in futuro da altre classi
	
		//device.setFullScreenWindow(frame);
	}
	
	
	
	
}
