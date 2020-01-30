module.exports = function(grunt) {

    // 1. Configuration

    grunt.initConfig({
        // pass in options to plugins, references to files, etc.

        json_minification: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'helpers',
                    src: ['ten_lists.json'],
                    dest: '.',
                    ext: '.json'
                }]
            }
        }

    });


    // 2. Load Plugins

    grunt.loadNpmTasks('grunt-json-minification');

    // 3. Register Tasks

    // grunt.registerTask('run', function(){
    // 	console.log('I am Running');
    // });

    // grunt.registerTask('walk', function(){
    // 	console.log('I am Walking');
    // });

    // grunt.registerTask('all', ['run', 'walk']);

    grunt.registerTask('compress-json', ['json_minification']);
    grunt.registerTask('default', 'compress-json');

};
