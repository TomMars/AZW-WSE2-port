from header_shaders import *

shaders = [
	("aon_lod_shader_noshading", "no_shading", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
	("aon_lod_shader_noshading_noalpha", "no_shading_no_alpha", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
	("aon_lod_shader_shaded", "diffuse_no_shadow", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
	("aon_lod_shader_shaded_noalpha", "diffuse_no_shadow_no_alpha", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
	("ctf_pennon_shader", "ctf_pennon_shader", "", shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"ctf_pennon_shader_nobump",
	]),
	("ctf_pennon_shader_nobump", "ctf_pennon_shader_nobump", "", shf_uses_diffuse_map, 0, []),
	("dot3_alpha_high", "dot3_high", "", shf_static_lighting|shf_uses_dot3|shf_uses_normal_map|shf_uses_diffuse_map, 0, [
		"dot3_alpha",
	]),
	("dot3_alpha_multitex_high", "dot3_multitex_high", "", shf_static_lighting|shf_uses_dot3|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_diffuse_2_map, 0, [
		"dot3_alpha_multitex",
	]),
	("dot3_alpha_multitex_parallax", "dot3_multitex_parallax", "", shf_static_lighting|shf_specular_enable|shf_uses_specular_map|shf_uses_dot3|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_diffuse_2_map, 0, [
		"dot3_multitex_parallax",
	]),
	("dot3_alpha_parallax", "dot3_parallax", "", shf_static_lighting|shf_specular_enable|shf_uses_specular_map|shf_uses_dot3|shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"dot3_alpha_high",
	]),
	("envmap_shader_Instanced_bump", "envmap_specular_diffuse_Instanced_bump", "", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_noskin_bump_colorspec_high",
	]),
	("envmap_shader_Instanced_bump_colorspec", "envmap_specular_diffuse_Instanced_bump_colorspec", "", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_noskin_bump_colorspec_high",
	]),
	("envmap_shader_Instanced_colorspec", "envmap_specular_diffuse_Instanced_colorspec", "", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_diffuse_map|shf_uses_environment_map, 0, [
		"envmap_shader_colorspec",
	]),
	("envmap_shader_colorspec", "envmap_specular_diffuse_colorspec", "", shf_specular_enable|shf_uses_specular_map|shf_uses_diffuse_map|shf_uses_environment_map, 0, []),
	("envmap_shader_noskin_bump", "envmap_specular_diffuse_noskin_bump", "envmap_specular_diffuse_skin_bump", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_bump_Instanced",
	]),
	("envmap_shader_noskin_bump_colorspec", "envmap_specular_diffuse_noskin_bump_colorspec", "envmap_specular_diffuse_skin_bump_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_bump_Instanced_colorspec",
	]),
	("envmap_shader_skin_bump", "envmap_specular_diffuse_skin_bump", "envmap_specular_diffuse_noskin_bump", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_skinning|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_skin_bump",
	]),
	("envmap_shader_skin_bump_colorspec", "envmap_specular_diffuse_skin_bump_colorspec", "envmap_specular_diffuse_noskin_bump_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_skinning|shf_uses_diffuse_map|shf_uses_environment_map, shrf_mid_quality, [
		"specular_shader_skin_bump_colorspec",
	]),
	("flag_shader", "flag_shader", "", shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"flag_shader_nobump",
	]),
	("flag_shader_nobump", "flag_shader_nobump", "", shf_uses_diffuse_map, 0, []),
	("flora_shader_bottomleftmove", "flora_bottomleftmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_bottommove", "flora_bottommove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_bottomrightmove", "flora_bottomrightmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_leftmove", "flora_leftmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_oimleavesmove", "flora_oimleavesmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_rightmove", "flora", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_sprucemove", "flora_sprucemove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_flowermove", "flora_flowermove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_topleftmove", "flora_topleftmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_topleftrightmove", "flora_topleftrightmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_topmove", "flora_topmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("flora_shader_toprightmove", "flora_toprightmove", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("hair_shader_aniso_noblend", "hair_shader_aniso_noblend", "", shf_special|shf_uses_normal_map|shf_uses_diffuse_map|shf_uses_diffuse_2_map, shrf_hi_quality, [
		"hair_shader_noblend",
	]),
	("hair_shader_noblend", "hair_shader_noblend", "", shf_special|shf_uses_diffuse_map|shf_uses_diffuse_2_map, 0, []),
	("pennon_shader", "pennon_shader", "", shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"pennon_shader_nobump",
	]),
	("pennon_shader_vertical", "pennon_vertical_shader", "", shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"pennon_vertical_shader_nobump",
	]),
	("pennon_shader_nobump", "pennon_shader_nobump", "", shf_uses_diffuse_map, 0, []),
	("pennon_shader_vertical_nobump", "pennon_vertical_shader_nobump", "", shf_uses_diffuse_map, 0, []),
	("plume_shader", "plume", "plume_skinned", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("plume_shader_skinned", "plume_skinned", "plume", shf_static_lighting|shf_uses_skinning|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("plume_shader_Instanced", "flora_Instanced", "", shf_static_lighting|shf_preshaded|shf_uses_instancing|shf_biased|shf_uses_diffuse_map, 0, [
		"plume_shader",
	]),
	("plume_shader_fakeskin", "plume", "plume", shf_static_lighting|shf_uses_skinning|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("plume_shader_move", "plume_move", "", shf_static_lighting|shf_preshaded|shf_biased|shf_uses_diffuse_map, 0, []),
	("sail_shader", "sail_shader", "", shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"sail_shader_nobump",
	]),
	("sail_shader_nobump", "sail_shader_nobump", "", shf_uses_diffuse_map, 0, []),
	("specular_shader_Instanced_colorspec", "standart_noskin_nobump_specmap_Instanced_colorspec", "standart_skin_nobump_specmap_colorspec", shf_special|shf_uses_diffuse_map, 0, [
		"specular_shader_colorspec",
	]),
	("specular_shader_bump_Instanced_colorspec", "standart_noskin_bump_specmap_Instanced_colorspec", "standart_skin_bump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map, 0, [
		"specular_shader_bump_colorspec",
	]),
	("specular_shader_bump_colorspec", "standart_noskin_bump_specmap_colorspec", "standart_skin_bump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"specular_shader",
	]),
	("specular_shader_colorspec", "standart_noskin_nobump_specmap_colorspec", "standart_skin_nobump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_diffuse_map, 0, [
		"tex_mul_color",
	]),
	("specular_shader_noskin_bump_colorspec_high", "standart_noskin_bump_specmap_colorspec", "standart_skin_bump_specmap_colorspec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"specular_shader_bump_colorspec",
	]),
	("specular_shader_noskin_bump_colorspec_high_Instanced", "standart_noskin_bump_specmap_high_Instanced_colorspec", "standart_skin_bump_specmap_colorspec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"specular_shader_noskin_bump_colorspec_high",
	]),
	("specular_shader_skin_bump_colorspec", "standart_skin_bump_specmap_colorspec", "standart_noskin_bump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_skinning|shf_uses_diffuse_map, shrf_mid_quality, [
		"specular_shader_skin_colorspec",
	]),
	("specular_shader_skin_bump_colorspec_high", "standart_skin_bump_specmap_colorspec_high", "standart_noskin_bump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_skinning|shf_uses_diffuse_map, shrf_hi_quality, [
		"specular_shader_skin_bump_colorspec",
	]),
	("specular_shader_skin_colorspec", "standart_skin_nobump_specmap_colorspec", "standart_noskin_nobump_specmap_colorspec", shf_specular_enable|shf_uses_specular_map|shf_uses_skinning|shf_uses_diffuse_map, 0, [
		"skeleton_shader",
	]),
	("standart_shader_bumpparallax_nospec_high", "standart_noskin_bumpparallax_nospec_high", "standart_skin_bump_nospec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_bumpparallaxfloor_nospec_high",
	]),
	("standart_shader_bumpparallaxfloor_nospec_high", "standart_noskin_bumpparallaxfloor_nospec_high", "standart_skin_bump_nospec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_mid_quality, [
		"standart_shader_bump_nospec",
	]),
	("standart_shader_bumpparallax_nospec_high_Instanced", "standart_noskin_bumpparallax_nospecmap_high_Instanced", "standart_noskin_bump_nospec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_bumpparallax_nospec_high",
	]),
	("standart_shader_bumpparallaxfloor_nospec_high_Instanced", "standart_noskin_bumpparallaxfloor_nospecmap_high_Instanced", "standart_noskin_bump_nospec_high", shf_specular_enable|shf_uses_specular_map|shf_uses_instancing|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_bumpparallax_nospec_high",
	]),
	("standart_shader_bumpparallax_nospec_high_noterraincolor", "standart_noskin_bumpparallax_nospec_high_noterraincolor", "", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_bump_nospec",
	]),
	("standart_shader_bumpparallaxfloor_nospec_high_noterraincolor", "standart_noskin_bumpparallaxfloor_nospec_high_noterraincolor", "", shf_specular_enable|shf_uses_specular_map|shf_uses_normal_map|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_bump_nospec",
	]),
	("standart_shader_nobump_nospec_high", "standart_noskin_nobump_nospec_high", "standart_skin_nobump_nospec_high", shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_nobump_nospec",
	]),
	("standart_shader_nobump_nospec_high_Instanced", "standart_noskin_nobump_nospec_high_Instanced", "standart_noskin_nobump_nospec_high", shf_uses_instancing|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_nobump_nospec_high",
	]),
	("standart_shader_nobump_nospec_high_noterraincolor", "standart_noskin_nobump_nospec_noterraincolor", "standart_skin_nobump_nospec_high_noterraincolor", shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_nobump_nospec_noterraincolor",
	]),
	("standart_shader_nobump_nospec_high_noterraincolor_Instanced", "standart_noskin_nobump_nospec_high_noterraincolor_Instanced", "", shf_uses_instancing|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_nobump_nospec_high_noterraincolor",
	]),
	("standart_shader_nobump_nospec_noterraincolor", "standart_noskin_nobump_nospec_noterraincolor", "standart_skin_nobump_nospec_noterraincolor", shf_uses_diffuse_map, 0, [
		"tex_mul_color_alpha",
	]),
	("standart_shader_nobump_nospec_noterraincolor_Instanced", "standart_noskin_nobump_nospecmap_noterraincolor_Instanced", "", shf_uses_instancing|shf_uses_diffuse_map, 0, [
		"standart_shader_nobump_nospec_noterraincolor",
	]),
	("standart_shader_skin_nobump_nospec_high", "standart_skin_nobump_nospec_high", "standart_noskin_nobump_nospec_high", shf_uses_skinning|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_skin_nobump_nospec",
	]),
	("standart_shader_skin_nobump_nospec_high_noterraincolor", "standart_skin_nobump_nospec_high_noterraincolor", "standart_noskin_nobump_nospec_noterraincolor", shf_uses_skinning|shf_uses_diffuse_map, shrf_hi_quality, [
		"standart_shader_skin_nobump_nospec_noterraincolor",
	]),
	("standart_shader_skin_nobump_nospec_noterraincolor", "standart_skin_nobump_nospec_noterraincolor", "standart_noskin_nobump_nospec_noterraincolor", shf_uses_skinning|shf_uses_diffuse_map, 0, [
		"specular_shader_skin",
	]),
	#AZW Reloaded
	("over_border_shader_failed", "skybox", "", shf_static_lighting|shf_preshaded|shf_uses_diffuse_map, 0, [
		"diffuse_no_shadow"
	]),
	("under_border_shader", "skybox", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
	("over_border_shader", "diffuse_no_shadow", "", shf_static_lighting|shf_uses_diffuse_map, 0, []),
]