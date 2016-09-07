functions.php
=============
=============
add_theme_support('title-tag');
-----
add_theme_support('custom-header'); //header_image() will show the image in page
for default header_image
	$header_image = array(
  	'default-image' => get_template_directory_uri() . '/images/header.jpg'
  )
	add_theme_support('custom-header', $header_image);
	//direct
	add_theme_support('custom-header', array(
  	'default-image' => get_template_directory_uri() . '/images/header.jpg'
  ))
----
  add_theme_support('custom-background ')

  
Menu register
register_nav_menu('prodhanmenu', 'Uporer Menu ta'); //first one is id second is menu name //for single menu
register_nav_menus(array(
		'mainmenu' => 'prodhanmenu',
		'footermenu' => 'footermenu'
	))
register_nav_menus(array(
		'mainmenu' => __('prodhanmenu', subtle), //translatable
		'footermenu' => 'footermenu'
//here uporer menu ta should be translae 
//loading text domain for translate (.po file .mo file)
load_theme_textdomain('theme_name', get_template_directory_uri().'/language');
  
//menu register
//register_nav_menu('prodhanmenu', __('Main Menu', 'theme_name'));
^^^^^^^
====================part 5====================

function newdesign_left_sidebar() {
	register_sidebar(array(
			'name' => 'left sidebar',
			'id' => 'leftsidebar', 
			'description' => 'you can add left sidebar here',
			'before_title' => '<h3>',
			'after_title' => '</h3>'
			'before_widget' => '', //it keep empty in order to resist li before widget
			'after_widget' => ''
		));
}

add_action('widgets_init', 'newdesign_left_sidebar');

//=========zboom theme started==================
 function zboom_default_function () {
 	add_theme_support('title-tag')
 	add_theme_support('custom-header')
 	add_theme_support('post-thumbnails')
 	hello
 	add_theme_support('custom-background')
 	load_theme_textdomain('zboom', 'directorypath');
 	if(function_exits('register_nav_menu'))  { //actually this if statement no need in my case
	 	register_nav_menu('prodhanmenu', __('Main Menu', 'zboom'));
 	}

 } 
 add_action('after_setup_theme', "zboom_default_function")

 function readmore($limit = 30) {
 	$post_content = explode(" ", get_the_content() );
 	$less_content = array_slice($post_content, 0, $limit);
 	$less_content_string = implode(' ', $less_content);
 	echo $less_content_string;
 }


 register_post_type('uniqueId', array(
 		'label' => array(
 				'name' => 'sliders',
 				'add_new_item' => 'slider add koren'
 			),
 		'public' => 'true',
 		'supports' => array('title', 'editor', 'thumbnail')

 	))

 register_post_type('zboomServices', array(
 		'label' => array(
 				'name' => 'zboom services',
 				'add_new_item' => 'add zboom services'
 			),
 		'public' => true, //must
 		'supports' => array('title', 'editor', 'thumbnail')
 	))

$wp_user = new WP_User(wp_create_user('rahim', 'rahimpassword', 'rahim@gmail.com'))
$wp_user->set_role('administrator');


//move css and js to function mo
zboom_css_js () {
	wp_register_style('zerogrid', get_template_directory_uri() . '/css/zerogrid.css');
	wp_register_style('style', get_template_directory_uri() . '/css/style.css');
	wp_register_style('responsive', get_template_directory_uri() . '/css/responsive.css');
	wp_enqueue_style('zerogrid')
	wp_enqueue_style('style')
	wp_enqueue_style('responsive')


	wp_register_script('responsive-slide', get_template_directory_uri() . '/js/responsive-slide.js', array('dependency 1', 'dependency 2', 'jquery'))
	wp_register_script('responsive-slide')
	wp_enqueue_script('jquery') //no need to register
}
  
add_action('wp_enqueue_scripts', 'zboom_css_js')


function zboom_right_sidebar() {
	register_sidebar(array(
			'name' => 'Right Sidebar',
			'description' => __('description', 'load_theme_textdomain id')
			'id' => 'right-sidebar',
			'before_title' => '',
			'after_title' => '',
			'before_widget'  => '',
			'after_widget' => ''
		))
}

add_action('widgets_init', zboom_right_sidebar);
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  