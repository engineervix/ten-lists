module.exports = function(grunt) {
    require("time-grunt")(grunt);
    // 1. Configuration

    grunt.initConfig({
        // pass in options to plugins, references to files, etc.

        json_minification: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'tenlists/utils',
                    src: ['ten_lists.json'],
                    dest: 'tenlists/data',
                    ext: '.json'
                }]
            }
        },

        copy: {
          fa: {
              expand: true,
              cwd: "node_modules/font-awesome/",
              src: ["css/*.css", "fonts/*"],
              dest: "tenlists/webapp/ten_lists/static/vendors/font-awesome/"
          },
          bootstrap: {
              expand: true,
              cwd: "node_modules/bootstrap/dist/",
              src: ["css/*.css", "js/*.js"],
              dest: "tenlists/webapp/ten_lists/static/vendors/bootstrap/"
          },
          // balloon_css: {
          //     expand: true,
          //     cwd: "node_modules/balloon-css/",
          //     src: ["*.css"],
          //     dest: "tenlists/webapp/ten_lists/static/vendors/balloon-css/"
          // },
          // bootswatch: {
          //     expand: true,
          //     cwd: "node_modules/bootswatch/dist/",
          //     src: ["**/*", "!**/*.scss"],
          //     dest: "tenlists/webapp/ten_lists/static/vendors/bootswatch/"
          // },
          // holderjs: {
          //     expand: true,
          //     cwd: "node_modules/holderjs/",
          //     src: ["holder.js", "holder.min.js"],
          //     dest: "tenlists/webapp/ten_lists/static/vendors/holderjs/"
          // },
          jquery: {
              expand: true,
              cwd: "node_modules/jquery/dist/",
              src: ["**/*", "!*.map"],
              dest: "tenlists/webapp/ten_lists/static/vendors/jquery/"
          },
          moment: {
              expand: true,
              cwd: "node_modules/moment/min/",
              src: ["**/*", "!*.map"],
              dest: "tenlists/webapp/ten_lists/static/vendors/moment/"
          }
      },

        cssmin: {
          dist: {
              files: [{
                  expand: true,
                  cwd: "tenlists/webapp/ten_lists/static/css/",
                  src: ["custom.css"],
                  dest: "tenlists/webapp/ten_lists/static/css/",
                  ext: ".min.css"
              }]
          }
      },

      uglify: {
        dist: {
            files: [{
                expand: true,
                cwd: "tenlists/webapp/ten_lists/static/js/",
                src: ["custom.js"],
                dest: "tenlists/webapp/ten_lists/static/js/",
                ext: ".min.js"
            }]
        }
    },

    watch: {
        css: {
            files: [
                "tenlists/webapp/ten_lists/static/css/custom.css"
            ],
            tasks: ["cssmin"]
        },
        js: {
            files: [
                "tenlists/webapp/ten_lists/static/js/custom.js"
            ],
            tasks: ["uglify"]
        }
    },

    clean: {
        dist: ["tenlists/webapp/ten_lists/static/vendors/*"]
    },

    browserSync: {
        dev: {
            bsFiles: {
                src: [
                    "tenlists/webapp/ten_lists/static/css/*.css",
                    "tenlists/webapp/ten_lists/static/js/*.js",
                    "tenlists/webapp/ten_lists/static/vendors/**/*.css",
                    "tenlists/webapp/ten_lists/static/vendors/**/*.js",
                    "tenlists/webapp/ten_lists/templates/**/*.html",
                    "tenlists/webapp/ten_lists/**/*.py"
                ]
            },
            options: {
                watchTask: true,
                proxy: "http://127.0.0.1:5000"
            }
        }
    }

    });

    // 2. Load Plugins

    grunt.loadNpmTasks('grunt-json-minification');
    grunt.loadNpmTasks("grunt-contrib-copy");
    grunt.loadNpmTasks("grunt-contrib-cssmin");
    grunt.loadNpmTasks("grunt-contrib-uglify-es");
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-browser-sync");
    grunt.loadNpmTasks("grunt-newer");


    // 3. Register Tasks

    // grunt.registerTask('run', function(){
    // 	console.log('I am Running');
    // });

    // grunt.registerTask('walk', function(){
    // 	console.log('I am Walking');
    // });

    // grunt.registerTask('all', ['run', 'walk']);

    grunt.registerTask('compress-json', ['json_minification']);
    grunt.registerTask("cp", ["newer:copy"]);
    grunt.registerTask("css-x", ["newer:cssmin"]);
    grunt.registerTask("js-x", ["newer:uglify"]);
    grunt.registerTask("rm", ["clean"]);
    grunt.registerTask("all", ["cp", "css-x", "js-x"]);
    grunt.registerTask("compress", ["css-x", "js-x"]);

    // default task
    grunt.registerTask("default", [
      "rm",
      "cp",
      "css-x",
      "js-x",
      "browserSync",
      "watch"
    ]);

    grunt.registerTask("sync", ["browserSync", "watch"]);

};
