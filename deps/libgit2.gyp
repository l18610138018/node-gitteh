{
  'targets': [{
    'target_name': 'libgit2',
    'type': 'static_library',

    'defines': [
      'GIT_THREADS',
      'SRC_UTIL_H_'
    ],

    'dependencies': [
      'zlib',
      'http_parser'
    ],

    'direct_dependent_settings': {
      'include_dirs': [
        'libgit2/include'
      ]
    },

    'include_dirs': [
      'libgit2/include',
      'libgit2/src',
      'libgit2/deps/regex'
    ],

    'sources': [
      'libgit2/src/array.h',
      'libgit2/src/attr_file.c',
      'libgit2/src/attr_file.h',
      'libgit2/src/attr.c',
      'libgit2/src/attr.h',
      'libgit2/src/blob.c',
      'libgit2/src/blob.h',
      'libgit2/src/branch.c',
      'libgit2/src/branch.h',
      'libgit2/src/bswap.h',
      'libgit2/src/buf_text.c',
      'libgit2/src/buf_text.h',
      'libgit2/src/buffer.c',
      'libgit2/src/buffer.h',
      'libgit2/src/cache.c',
      'libgit2/src/cache.h',
      'libgit2/src/cc-compact.h',
      'libgit2/src/checkout.c',
      'libgit2/src/checkout.h',
      'libgit2/src/clone.c',
      'libgit2/src/commit_list.c',
      'libgit2/src/commit_list.h',
      'libgit2/src/commit.c',
      'libgit2/src/commit.h',
      'libgit2/src/common.h',
      'libgit2/src/compress.c',
      'libgit2/src/compress.h',
      'libgit2/src/config_cache.c',
      'libgit2/src/config_file.c',
      'libgit2/src/config_file.h',
      'libgit2/src/config.c',
      'libgit2/src/config.h',
      'libgit2/src/crlf.c',
      'libgit2/src/date.c',
      'libgit2/src/delta-apply.c',
      'libgit2/src/delta-apply.h',
      'libgit2/src/delta.c',
      'libgit2/src/delta.h',
      'libgit2/src/diff_driver.c',
      'libgit2/src/diff_driver.h',
      'libgit2/src/diff_file.c',
      'libgit2/src/diff_file.h',
      'libgit2/src/diff_patch.c',
      'libgit2/src/diff_patch.h',
      'libgit2/src/diff_print.c',
      'libgit2/src/diff_tform.c',
      'libgit2/src/diff_xdiff.c',
      'libgit2/src/diff_xdiff.h',
      'libgit2/src/diff.c',
      'libgit2/src/diff.h',
      'libgit2/src/errors.c',
      'libgit2/src/fetch.c',
      'libgit2/src/fetch.h',
      'libgit2/src/fetchhead.c',
      'libgit2/src/fetchhead.h',
      'libgit2/src/filebuf.c',
      'libgit2/src/filebuf.h',
      'libgit2/src/fileops.c',
      'libgit2/src/fileops.h',
      'libgit2/src/filter.c',
      'libgit2/src/filter.h',
      'libgit2/src/fnmatch.c',
      'libgit2/src/fnmatch.h',
      'libgit2/src/global.c',
      'libgit2/src/global.h',
      'libgit2/src/graph.c',
      'libgit2/src/hash.c',
      'libgit2/src/hash.h',
      'libgit2/src/hashsig.c',
      'libgit2/src/hashsig.h',
      'libgit2/src/ignore.c',
      'libgit2/src/ignore.h',
      'libgit2/src/index.c',
      'libgit2/src/index.h',
      'libgit2/src/indexer.c',
      'libgit2/src/iterator.c',
      'libgit2/src/iterator.h',
      'libgit2/src/khash.h',
      'libgit2/src/map.h',
      'libgit2/src/merge_file.c',
      'libgit2/src/merge_file.h',
      'libgit2/src/merge.c',
      'libgit2/src/merge.h',
      'libgit2/src/message.c',
      'libgit2/src/message.h',
      'libgit2/src/mwindow.c',
      'libgit2/src/mwindow.h',
      'libgit2/src/netops.c',
      'libgit2/src/netops.h',
      'libgit2/src/notes.c',
      'libgit2/src/notes.h',
      'libgit2/src/object_api.c',
      'libgit2/src/object.c',
      'libgit2/src/object.h',
      'libgit2/src/odb_loose.c',
      'libgit2/src/odb_pack.c',
      'libgit2/src/odb.c',
      'libgit2/src/odb.h',
      'libgit2/src/offmap.h',
      'libgit2/src/oid.c',
      'libgit2/src/oid.h',
      'libgit2/src/oidmap.h',
      'libgit2/src/pack-objects.c',
      'libgit2/src/pack-objects.h',
      'libgit2/src/pack.c',
      'libgit2/src/pack.h',
      'libgit2/src/path.c',
      'libgit2/src/path.h',
      'libgit2/src/pathspec.c',
      'libgit2/src/pathspec.h',
      'libgit2/src/pool.c',
      'libgit2/src/pool.h',
      'libgit2/src/posix.c',
      'libgit2/src/posix.h',
      'libgit2/src/pqueue.c',
      'libgit2/src/pqueue.h',
      'libgit2/src/push.c',
      'libgit2/src/push.h',
      'libgit2/src/refdb_fs.c',
      'libgit2/src/refdb_fs.h',
      'libgit2/src/refdb.c',
      'libgit2/src/refdb.h',
      'libgit2/src/reflog.c',
      'libgit2/src/reflog.h',
      'libgit2/src/refs.c',
      'libgit2/src/refs.h',
      'libgit2/src/refspec.c',
      'libgit2/src/refspec.h',
      'libgit2/src/remote.c',
      'libgit2/src/remote.h',
      'libgit2/src/repo_template.h',
      'libgit2/src/repository.c',
      'libgit2/src/repository.h',
      'libgit2/src/reset.c',
      'libgit2/src/revparse.c',
      'libgit2/src/revwalk.c',
      'libgit2/src/revwalk.h',
      'libgit2/src/sha1_lookup.c',
      'libgit2/src/sha1_lookup.h',
      'libgit2/src/signature.c',
      'libgit2/src/signature.h',
      'libgit2/src/stash.c',
      'libgit2/src/status.c',
      'libgit2/src/status.h',
      'libgit2/src/strmap.h',
      'libgit2/src/submodule.c',
      'libgit2/src/submodule.h',
      'libgit2/src/tag.c',
      'libgit2/src/tag.h',
      'libgit2/src/thread-utils.c',
      'libgit2/src/thread-utils.h',
      'libgit2/src/trace.c',
      'libgit2/src/trace.h',
      'libgit2/src/transport.c',
      'libgit2/src/tree-cache.c',
      'libgit2/src/tree-cache.h',
      'libgit2/src/tree.c',
      'libgit2/src/tree.h',
      'libgit2/src/tsort.c',
      'libgit2/src/util.c',
      'libgit2/src/util.h',
      'libgit2/src/vector.c',
      'libgit2/src/vector.h',
      'libgit2/src/transports/cred_helpers.c',
      'libgit2/src/transports/cred.c',
      'libgit2/src/transports/git.c',
      'libgit2/src/transports/http.c',
      'libgit2/src/transports/local.c',
      'libgit2/src/transports/smart_pkt.c',
      'libgit2/src/transports/smart_protocol.c',
      'libgit2/src/transports/smart.c',
      'libgit2/src/transports/smart.h',
      'libgit2/src/transports/ssh.c',
      'libgit2/src/transports/winhttp.c',
      'libgit2/src/xdiff/xdiff.h',
      'libgit2/src/xdiff/xdiffi.c',
      'libgit2/src/xdiff/xdiffi.h',
      'libgit2/src/xdiff/xemit.c',
      'libgit2/src/xdiff/xemit.h',
      'libgit2/src/xdiff/xhistogram.c',
      'libgit2/src/xdiff/xinclude.h',
      'libgit2/src/xdiff/xmacros.h',
      'libgit2/src/xdiff/xmerge.c',
      'libgit2/src/xdiff/xpatience.c',
      'libgit2/src/xdiff/xprepare.c',
      'libgit2/src/xdiff/xprepare.h',
      'libgit2/src/xdiff/xtypes.h',
      'libgit2/src/xdiff/xutils.c',
      'libgit2/src/xdiff/xutils.h'
    ],

    'conditions': [
      ["OS=='linux'", {
        'cflags': [
          '-w'
        ]
      }],

      ["OS!='win'", {
        'libraries': [
          '-lpthread'
        ],

        'sources': [
          'libgit2/src/unix/map.c',
          'libgit2/src/unix/posix.h',
          'libgit2/src/unix/realpath.c'
        ],

        'cflags': [
          '-Wno-missing-field-initializers',
          '-Wno-unused-variable'
        ],

        'xcode_settings': {
          'WARNING_CFLAGS': [
            '-Wno-missing-field-initializers',
            '-Wno-unused-variable'
          ]
        }
      }]
    ]
  }, {
    'target_name': 'zlib',
    'type': 'static_library',

    'defines': [
      'NO_VIZ',
      'STDC',
      'NO_GZIP'
    ],

    'include_dirs': [
      'libgit2/include/',
      'libgit2/deps/regex/'
    ],

    'direct_dependent_settings': {
      'include_dirs': [
        'libgit2/deps/zlib'
      ]
    },

    'sources': [
      'libgit2/deps/zlib/adler32.c',
      'libgit2/deps/zlib/crc32.c',
      'libgit2/deps/zlib/crc32.h',
      'libgit2/deps/zlib/deflate.c',
      'libgit2/deps/zlib/deflate.h',
      'libgit2/deps/zlib/inffast.c',
      'libgit2/deps/zlib/inffast.h',
      'libgit2/deps/zlib/inffixed.h',
      'libgit2/deps/zlib/inflate.c',
      'libgit2/deps/zlib/inflate.h',
      'libgit2/deps/zlib/inftrees.c',
      'libgit2/deps/zlib/inftrees.h',
      'libgit2/deps/zlib/trees.c',
      'libgit2/deps/zlib/tree.h',
      'libgit2/deps/zlib/zconf.h',
      'libgit2/deps/zlib/zlib.h',
      'libgit2/deps/zlib/zutil.c',
      'libgit2/deps/zlib/zutil.h'
    ]
  }, {
    'target_name': 'http_parser',
    'type': 'static_library',

    'direct_dependent_settings': {
      'include_dirs': [
        'libgit2/deps/http-parser'
      ]
    },

    'sources': [
      'libgit2/deps/http-parser/http_parser.c',
      'libgit2/deps/http-parser/http_parser.h'
    ],

    'conditions': [
      ["OS=='win'", {
        'msvs_disabled_warnings': [
          4244 # conversion from 'ssize_t' to 'int32_t' , possible loss of data
        ]
      }]
    ]
  }]
}
