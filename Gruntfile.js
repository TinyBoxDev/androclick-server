/**
 *  _____ _            ______            ______ 
 * |_   _(_)           | ___ \           |  _  \
 *   | |  _ _ __  _   _| |_/ / _____  __ | | | |_____   __
 *   | | | | '_ \| | | | ___ \/ _ \ \/ / | | | / _ \ \ / /
 *   | | | | | | | |_| | |_/ / (_) >  <  | |/ /  __/\ V /
 *   \_/ |_|_| |_|\__, \____/ \___/_/\_\ |___/ \___| \_/
 *                __/ |
 *               |___/
 *
 * Gruntfile for Androclick Server
 **/

module.exports = function(grunt) {

  grunt.initConfig({
    srcFiles: [ 'lib/**/*.js' ],
    testFiles: [ 'test/**/*.test.js' ],
    allFiles: [ '<%= srcFiles %>', '<%= testFiles %>', 'Gruntfile.js' ],

    jshint: {
      options: {
        node: true,
      },
      files: ['<%= allFiles %>']
    },

    mochaTest: {
      unit: {
        options: {
          reporter: 'spec'
        },
        src: ['<%= testFiles %>']
      }
    },

    watch: {
      files: ['<%= allFiles %>'],
      tasks: ['test']
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-mocha-test');

  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('test', ['jshint', 'mochaTest:unit']);
};
