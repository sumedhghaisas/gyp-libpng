{    
    'targets': [
    {
      'target_name': 'png_test',
      'dependencies': [
        '../bindings/libpng.gyp:libpng'
      ],
      'sources': [
        'pngtest.c',
      ],
      "include_dirs": [
        "../libpng",
        "../gyp-zlib/zlib/",
	"../config/<(OS)/<(target_arch)"
      ],
    }
  ]
}
