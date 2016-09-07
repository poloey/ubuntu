index.php
style.css
in style.css write following thing
===================================
  /*
Theme Name: Twenty Thirteen
Theme URI: http://wordpress.org/themes/twentythirteen
Author: the WordPress team
Author URI: http://wordpress.org/
Description: The 2013 theme for WordPress takes us back to the blog, featuring a full range of post formats, each displayed beautifully in their own unique way. Design details abound, starting with a vibrant color scheme and matching header images, beautiful typography and icons, and a flexible layout that looks great on any device, big or small.
Version: 1.0
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: black, brown, orange, tan, white, yellow, light, one-column, two-columns, right-sidebar, flexible-width, custom-header, custom-menu, editor-style, featured-images, microformats, post-formats, rtl-language-support, sticky-post, translation-ready
Text Domain: twentythirteen

This theme, like WordPress, is licensed under the GPL.
Use it to make something cool, have fun, and share what you've learned with others.
*/
  ==========================
  
screenshot.png

bloginfo('template_directory') +
bloginfo('template_url') +
bloginfo('stylesheet_url')
bloginfo('name');
bloginfo('description');

echo get_template_directory_uri();
esc_url(get_template_directory_uri());
wp_head()
wp_footer()

header_image();
//<body class=<?php body_class() ?> >
wp_nav_menu()

wp_nav_menu(array(
    'theme_location' => 'prodhanmenu'
  ))
wp_nav_menu(array(
    'theme_location' => 'footerMenu'
  ))
  
<?php while(have_posts() ) : the_post();?>
the_post_thumbnail();
h1 > the_title();
content > the_content();

<?php endwhile;  ?>

.current-menu-item a {
  //active style in css
}
add_theme_support('post-thumbnails')
page.php
footer.php
get_header();
get_footer();
page.php > single.php
the_permalink();
^^^^^^^
=======================part 5==================
dyanamic_sidebar('leftsidebar')

//=================zboom theme started============
index.php 
style.css > comment 
screenshot.php 600x450


language_attributes();
bloginfo('charset')
bloginfo('description')
echo esc_url(get_template_directory_uri()) /image
wp_head()
wp_footer()
body_class();

wp_nav_menu(array(
    'theme_location' => 'prodhanmenu'
  ))

.current-menu-item{appriate style}

<?php while(have_posts()) : the_post()?>
the_title()
the_post_thumbnail();
the_content()
the_permalink()
the_author();
the_time('F d, Y')
comments_popup_link();
comments_popup_link('comment nai', 'akta comment ace', '% comment', 'comment class', 'disabled comment');
<?php endwhile;

single.php
header.php
footer.php
get_header()
get_footer();
comments_template();
page.php

custom page > frontpage.php
php comment like inside style.css 
/*
Template Name : Home
 */
//for register post type
$sliderItems = new WP_Query(array(
    'post_type' => 'uniqueId of register_post_type',
    'posts_per_page' => 3 //remove it if you want unlimited
  ))
while($sliderItems->have_posts()) : $sliderItems->the_post();
  //content stuff will be as usal
endwhile

$zboomServices = new WP_Query(array(
    'post_type' => 'zboomServices',
    'posts_per_page' => 3
  ))

while($zboomServices->have_posts()) : $zboomServices->the_post()
  //content stuff will be as usal
endwhile


//default query page
$post_contents = new WP_Query(array(
    'post_type' => 'post',
    'posts_per_page' => 4
  ))
while($post_contents->have_posts()) : $post_contents->the_post()
  //content stuff will be as usal
endwhile
//
sidebar.php
dyanamic_sidebar('right-sidebar')

get_search_form(); //following code working fine 

<form action="esc_url(bloginfo('home'))" method="GET">
  <input type="text" name="s" id=""/>
</form>

the_posts_navigation();
the_posts_navigation(array(
    'prev_text' => 'parerta',
    'next_text' => 'agerta',
    'screen_reader_text' => 'some screen reader text' //space rakhle kicui show karbena
  ))
the_posts_pagination(array(
    'prev_text' => 'parerta',
    'next_text' => 'agerta',
    'screen_reader_text' => 'some screen reader text' //space rakhle kicui show karbena,
    'show_all' => true //if you don't want to ... inside pagination,
    'before_page_number' => '<li>',
    'after_page_number' => '</li>'
  ))



  







