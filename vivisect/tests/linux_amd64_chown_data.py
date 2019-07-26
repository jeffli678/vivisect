chown_data = {
    'imports' : [
        (0x220fd80, 8, 9, '*.endgrent'),
        (0x220fd88, 8, 9, '*.__uflow'),
        (0x220fd90, 8, 9, '*.getenv'),
        (0x220fd98, 8, 9, '*.abort'),
        (0x220fda0, 8, 9, '*.__errno_location'),
        (0x220fda8, 8, 9, '*.strncmp'),
        (0x220fdb0, 8, 9, '*._exit'),
        (0x220fdb8, 8, 9, '*.strcpy'),
        (0x220fdc0, 8, 9, '*.__fpending'),
        (0x220fdc8, 8, 9, '*.qsort'),
        (0x220fdd0, 8, 9, '*.fcntl'),
        (0x220fdd8, 8, 9, '*.textdomain'),
        (0x220fde0, 8, 9, '*.fclose'),
        (0x220fde8, 8, 9, '*.getpwuid'),
        (0x220fdf0, 8, 9, '*.bindtextdomain'),
        (0x220fdf8, 8, 9, '*.stpcpy'),
        (0x220fe00, 8, 9, '*.dcgettext'),
        (0x220fe08, 8, 9, '*.__ctype_get_mb_cur_max'),
        (0x220fe10, 8, 9, '*.strlen'),
        (0x220fe18, 8, 9, '*.__lxstat'),
        (0x220fe20, 8, 9, '*.openat'),
        (0x220fe28, 8, 9, '*.__stack_chk_fail'),
        (0x220fe30, 8, 9, '*.getopt_long'),
        (0x220fe38, 8, 9, '*.mbrtowc'),
        (0x220fe40, 8, 9, '*.strchr'),
        (0x220fe48, 8, 9, '*.getgrgid'),
        (0x220fe50, 8, 9, '*.__fxstatat'),
        (0x220fe58, 8, 9, '*.strrchr'),
        (0x220fe60, 8, 9, '*.lseek'),
        (0x220fe68, 8, 9, '*.__assert_fail'),
        (0x220fe70, 8, 9, '*.memset'),
        (0x220fe78, 8, 9, '*.fscanf'),
        (0x220fe80, 8, 9, '*.close'),
        (0x220fe88, 8, 9, '*.__openat_2'),
        (0x220fe90, 8, 9, '*.closedir'),
        (0x220fe98, 8, 9, '*.memcmp'),
        (0x220fea0, 8, 9, '*.fputs_unlocked'),
        (0x220fea8, 8, 9, '*.calloc'),
        (0x220feb0, 8, 9, '*.strcmp'),
        (0x220feb8, 8, 9, '*.dirfd'),
        (0x220fec0, 8, 9, '*.getpwnam'),
        (0x220fec8, 8, 9, '*.memcpy'),
        (0x220fed0, 8, 9, '*.getgrnam'),
        (0x220fed8, 8, 9, '*.fileno'),
        (0x220fee0, 8, 9, '*.__xstat'),
        (0x220fee8, 8, 9, '*.readdir'),
        (0x220fef0, 8, 9, '*.malloc'),
        (0x220fef8, 8, 9, '*.fflush'),
        (0x220ff00, 8, 9, '*.nl_langinfo'),
        (0x220ff08, 8, 9, '*.ungetc'),
        (0x220ff10, 8, 9, '*.__fxstat'),
        (0x220ff18, 8, 9, '*.endpwent'),
        (0x220ff20, 8, 9, '*.__freading'),
        (0x220ff28, 8, 9, '*.fchdir'),
        (0x220ff30, 8, 9, '*.realloc'),
        (0x220ff38, 8, 9, '*.fdopen'),
        (0x220ff40, 8, 9, '*.setlocale'),
        (0x220ff48, 8, 9, '*.__printf_chk'),
        (0x220ff50, 8, 9, '*.memmove'),
        (0x220ff58, 8, 9, '*.error'),
        (0x220ff60, 8, 9, '*.open'),
        (0x220ff68, 8, 9, '*.fseeko'),
        (0x220ff70, 8, 9, '*.fchown'),
        (0x220ff78, 8, 9, '*.fdopendir'),
        (0x220ff80, 8, 9, '*.strtoul'),
        (0x220ff88, 8, 9, '*.fstatfs'),
        (0x220ff90, 8, 9, '*.__cxa_atexit'),
        (0x220ff98, 8, 9, '*.fchownat'),
        (0x220ffa0, 8, 9, '*.exit'),
        (0x220ffa8, 8, 9, '*.fwrite'),
        (0x220ffb0, 8, 9, '*.__fprintf_chk'),
        (0x220ffb8, 8, 9, '*.mbsinit'),
        (0x220ffc0, 8, 9, '*.iswprint'),
        (0x220ffc8, 8, 9, '*.__ctype_b_loc'),
        (0x220ffd0, 8, 9, '*.free'),
        (0x220ffd8, 8, 9, '*._ITM_deregisterTMCloneTable'),
        (0x220ffe0, 8, 9, '*.__libc_start_main'),
        (0x220ffe8, 8, 9, '*.__gmon_start__'),
        (0x220fff0, 8, 9, '*._ITM_registerTMCloneTable'),
        (0x220fff8, 8, 9, '*.__cxa_finalize'),
    ],

    'exports' : [
        (0x20027a0, 0, '__entry', 'chown'),
        (0x2008420, 0, 'fts_open', 'chown'),
        (0x20087c0, 0, 'fts_close', 'chown'),
        (0x2008950, 0, 'fts_read', 'chown'),
        (0x20090d0, 0, 'fts_set', 'chown'),
        (0x2009100, 0, 'fts_children', 'chown'),
        (0x200b0a0, 1, '_IO_stdin_used', 'chown'),
        (0x200c5e0, 1, 'quoting_style_vals', 'chown'),
        (0x200c960, 1, 'version_etc_copyright', 'chown'),
        (0x220fb20, 1, 'quoting_style_args', 'chown'),
        (0x2210010, 1, 'Version', 'chown'),
        (0x2210018, 1, 'exit_failure', 'chown'),
        (0x2210020, 1, 'quote_quoting_options', 'chown'),
        (0x2210080, 1, '__progname', 'chown'),
        (0x2210080, 1, 'program_invocation_short_name', 'chown'),
        (0x2210088, 1, 'stdout', 'chown'),
        (0x2210090, 1, 'optind', 'chown'),
        (0x22100a0, 1, 'optarg', 'chown'),
        (0x22100a8, 1, '__progname_full', 'chown'),
        (0x22100a8, 1, 'program_invocation_name', 'chown'),
        (0x22100c0, 1, 'stderr', 'chown'),
        (0x22100f8, 1, 'program_name', 'chown'),
        (0x6572006b6a635f66, 0, '', 'chown'),
    ],

    'relocs' : [
        ('chown', 0x20f950, 2, 0x28a0),
        ('chown', 0x20f958, 2, 0x2860),
        ('chown', 0x20f960, 2, 0xb19a),
        ('chown', 0x20f980, 2, 0xb1a4),
        ('chown', 0x20f9a0, 2, 0xb1b4),
        ('chown', 0x20f9c0, 2, 0xb1ac),
        ('chown', 0x20f9e0, 2, 0xb1b1),
        ('chown', 0x20fa00, 2, 0xb1c0),
        ('chown', 0x20fa20, 2, 0xb1c3),
        ('chown', 0x20fa40, 2, 0xb1d1),
        ('chown', 0x20fa60, 2, 0xb1d7),
        ('chown', 0x20fa80, 2, 0xb1b6),
        ('chown', 0x20faa0, 2, 0xb1de),
        ('chown', 0x20fac0, 2, 0xb1e6),
        ('chown', 0x20fae0, 2, 0xb1eb),
        ('chown', 0x20fb20, 2, 0xc141),
        ('chown', 0x20fb28, 2, 0xc149),
        ('chown', 0x20fb30, 2, 0xc14f),
        ('chown', 0x20fb38, 2, 0xc15c),
        ('chown', 0x20fb40, 2, 0xc169),
        ('chown', 0x20fb48, 2, 0xcb40),
        ('chown', 0x20fb50, 2, 0xc17d),
        ('chown', 0x20fb58, 2, 0xc162),
        ('chown', 0x20fb60, 2, 0xb13d),
        ('chown', 0x20fb68, 2, 0xc185),
        ('chown', 0x210008, 2, 0x210008),
        ('chown', 0x210010, 2, 0xc0d4),
        ('chown', 0x210060, 2, 0x210070),
        ('chown', 0x210078, 2, 0x210100),
    ],

    'names' : [
        (0x2000238, 'str_/lib64/ld-linux-_02000238'),
        (0x2000ce1, 'str_libc.so.6_02000ce1'),
        (0x2000ceb, 'str_fflush_02000ceb'),
        (0x2000cf2, 'str_strcpy_02000cf2'),
        (0x2000cf9, 'str___printf_chk_02000cf9'),
        (0x2000d06, 'str_readdir_02000d06'),
        (0x2000d0e, 'str_setlocale_02000d0e'),
        (0x2000d18, 'str_mbrtowc_02000d18'),
        (0x2000d20, 'str_strncmp_02000d20'),
        (0x2000d28, 'str_optind_02000d28'),
        (0x2000d2f, 'str_strrchr_02000d2f'),
        (0x2000d37, 'str_dcgettext_02000d37'),
        (0x2000d41, 'str_getpwuid_02000d41'),
        (0x2000d4a, 'str_closedir_02000d4a'),
        (0x2000d53, 'str_fchdir_02000d53'),
        (0x2000d5a, 'str_getgrgid_02000d5a'),
        (0x2000d63, 'str_error_02000d63'),
        (0x2000d69, 'str___stack_chk_fail_02000d69'),
        (0x2000d7a, 'str___lxstat_02000d7a'),
        (0x2000d83, 'str_iswprint_02000d83'),
        (0x2000d8c, 'str_realloc_02000d8c'),
        (0x2000d94, 'str_fstatfs_02000d94'),
        (0x2000d9c, 'str_abort_02000d9c'),
        (0x2000da2, 'str__exit_02000da2'),
        (0x2000da8, 'str_program_invocati_02000da8'),
        (0x2000dc0, 'str___assert_fail_02000dc0'),
        (0x2000dce, 'str___ctype_get_mb_c_02000dce'),
        (0x2000de5, 'str_endpwent_02000de5'),
        (0x2000dee, 'str_fts_close_02000dee'),
        (0x2000df8, 'str_getpwnam_02000df8'),
        (0x2000e01, 'str_calloc_02000e01'),
        (0x2000e08, 'str_strlen_02000e08'),
        (0x2000e0f, 'str_ungetc_02000e0f'),
        (0x2000e16, 'str_memset_02000e16'),
        (0x2000e1d, 'str___errno_location_02000e1d'),
        (0x2000e2e, 'str_memcmp_02000e2e'),
        (0x2000e35, 'str_endgrent_02000e35'),
        (0x2000e3e, 'str___fprintf_chk_02000e3e'),
        (0x2000e4c, 'str_getgrnam_02000e4c'),
        (0x2000e55, 'str_fchown_02000e55'),
        (0x2000e5c, 'str_stdout_02000e5c'),
        (0x2000e63, 'str_fts_read_02000e63'),
        (0x2000e6c, 'str_lseek_02000e6c'),
        (0x2000e72, 'str_memcpy_02000e72'),
        (0x2000e79, 'str_fclose_02000e79'),
        (0x2000e80, 'str_strtoul_02000e80'),
        (0x2000e88, 'str_malloc_02000e88'),
        (0x2000e8f, 'str_fdopendir_02000e8f'),
        (0x2000e99, 'str___openat_2_02000e99'),
        (0x2000ea4, 'str_mbsinit_02000ea4'),
        (0x2000eac, 'str___uflow_02000eac'),
        (0x2000eb4, 'str_nl_langinfo_02000eb4'),
        (0x2000ec0, 'str___ctype_b_loc_02000ec0'),
        (0x2000ece, 'str_getenv_02000ece'),
        (0x2000ed5, 'str_fts_set_02000ed5'),
        (0x2000edd, 'str_optarg_02000edd'),
        (0x2000ee4, 'str___freading_02000ee4'),
        (0x2000eef, 'str_stderr_02000eef'),
        (0x2000ef6, 'str_fchownat_02000ef6'),
        (0x2000eff, 'str_fscanf_02000eff'),
        (0x2000f06, 'str_getopt_long_02000f06'),
        (0x2000f12, 'str___fxstat_02000f12'),
        (0x2000f1b, 'str_fileno_02000f1b'),
        (0x2000f22, 'str_fwrite_02000f22'),
        (0x2000f29, 'str___fpending_02000f29'),
        (0x2000f34, 'str_strchr_02000f34'),
        (0x2000f3b, 'str_program_invocati_02000f3b'),
        (0x2000f59, 'str_fdopen_02000f59'),
        (0x2000f60, 'str_qsort_02000f60'),
        (0x2000f66, 'str___cxa_finalize_02000f66'),
        (0x2000f75, 'str_fts_open_02000f75'),
        (0x2000f7e, 'str_fcntl_02000f7e'),
        (0x2000f84, 'str_openat_02000f84'),
        (0x2000f8b, 'str___xstat_02000f8b'),
        (0x2000f93, 'str_memmove_02000f93'),
        (0x2000f9b, 'str_bindtextdomain_02000f9b'),
        (0x2000faa, 'str___fxstatat_02000faa'),
        (0x2000fb5, 'str_fts_children_02000fb5'),
        (0x2000fc2, 'str_strcmp_02000fc2'),
        (0x2000fc9, 'str___libc_start_mai_02000fc9'),
        (0x2000fdb, 'str_dirfd_02000fdb'),
        (0x2000fe1, 'str_stpcpy_02000fe1'),
        (0x2000fe8, 'str_fseeko_02000fe8'),
        (0x2000fef, 'str_fputs_unlocked_02000fef'),
        (0x2000ffe, 'str_free_02000ffe'),
        (0x2001003, 'str___progname_02001003'),
        (0x200100e, 'str___progname_full_0200100e'),
        (0x200101e, 'str___cxa_atexit_0200101e'),
        (0x200102b, 'str_quote_quoting_op_0200102b'),
        (0x2001041, 'str_Version_02001041'),
        (0x2001049, 'str__IO_stdin_used_02001049'),
        (0x2001058, 'str_quoting_style_va_02001058'),
        (0x200106b, 'str_quoting_style_ar_0200106b'),
        (0x200107e, 'str_exit_failure_0200107e'),
        (0x200108b, 'str_program_name_0200108b'),
        (0x2001098, 'str_version_etc_copy_02001098'),
        (0x20010ae, 'str_GLIBC_2.3_020010ae'),
        (0x20010b8, 'str_GLIBC_2.3.4_020010b8'),
        (0x20010c4, 'str_GLIBC_2.14_020010c4'),
        (0x20010cf, 'str_GLIBC_2.7_020010cf'),
        (0x20010d9, 'str_GLIBC_2.4_020010d9'),
        (0x20010e3, 'str_GLIBC_2.2.5_020010e3'),
        (0x20010ef, 'str__ITM_deregisterT_020010ef'),
        (0x200110b, 'str___gmon_start___0200110b'),
        (0x200111a, 'str__ITM_registerTMC_0200111a'),
        (0x2001d38, 'chown.init_function'),
        (0x2001d60, 'endgrent_02001d60'),
        (0x2001d70, '__uflow_02001d70'),
        (0x2001d80, 'getenv_02001d80'),
        (0x2001d90, 'abort_02001d90'),
        (0x2001da0, '__errno_location_02001da0'),
        (0x2001db0, 'strncmp_02001db0'),
        (0x2001dc0, '_exit_02001dc0'),
        (0x2001dd0, 'strcpy_02001dd0'),
        (0x2001de0, '__fpending_02001de0'),
        (0x2001df0, 'qsort_02001df0'),
        (0x2001e00, 'fcntl_02001e00'),
        (0x2001e10, 'textdomain_02001e10'),
        (0x2001e20, 'fclose_02001e20'),
        (0x2001e30, 'getpwuid_02001e30'),
        (0x2001e40, 'bindtextdomain_02001e40'),
        (0x2001e50, 'stpcpy_02001e50'),
        (0x2001e60, 'dcgettext_02001e60'),
        (0x2001e70, '__ctype_get_mb_cur_max_02001e70'),
        (0x2001e80, 'strlen_02001e80'),
        (0x2001e90, '__lxstat_02001e90'),
        (0x2001ea0, 'openat_02001ea0'),
        (0x2001eb0, '__stack_chk_fail_02001eb0'),
        (0x2001ec0, 'getopt_long_02001ec0'),
        (0x2001ee0, 'strchr_02001ee0'),
        (0x2001ef0, 'getgrgid_02001ef0'),
        (0x2001f00, '__fxstatat_02001f00'),
        (0x2001f10, 'strrchr_02001f10'),
        (0x2001f20, 'lseek_02001f20'),
        (0x2001f30, '__assert_fail_02001f30'),
        (0x2001f40, 'memset_02001f40'),
        (0x2001f50, 'fscanf_02001f50'),
        (0x2001f60, 'close_02001f60'),
        (0x2001f70, '__openat_2_02001f70'),
        (0x2001f80, 'closedir_02001f80'),
        (0x2001fa0, 'fputs_unlocked_02001fa0'),
        (0x2001fb0, 'calloc_02001fb0'),
        (0x2001fc0, 'strcmp_02001fc0'),
        (0x2001fd0, 'dirfd_02001fd0'),
        (0x2001fe0, 'getpwnam_02001fe0'),
        (0x2001ff0, 'memcpy_02001ff0'),
        (0x2002000, 'getgrnam_02002000'),
        (0x2002010, 'fileno_02002010'),
        (0x2002020, '__xstat_02002020'),
        (0x2002030, 'readdir_02002030'),
        (0x2002040, 'malloc_02002040'),
        (0x2002060, 'nl_langinfo_02002060'),
        (0x2002070, 'ungetc_02002070'),
        (0x2002080, '__fxstat_02002080'),
        (0x2002090, 'endpwent_02002090'),
        (0x20020a0, '__freading_020020a0'),
        (0x20020b0, 'fchdir_020020b0'),
        (0x20020c0, 'realloc_020020c0'),
        (0x20020d0, 'fdopen_020020d0'),
        (0x20020e0, 'setlocale_020020e0'),
        (0x20020f0, '__printf_chk_020020f0'),
        (0x2002100, 'memmove_02002100'),
        (0x2002110, 'error_02002110'),
        (0x2002120, 'open_02002120'),
        (0x2002140, 'fchown_02002140'),
        (0x2002150, 'fdopendir_02002150'),
        (0x2002160, 'strtoul_02002160'),
        (0x2002170, 'fstatfs_02002170'),
        (0x2002190, 'fchownat_02002190'),
        (0x20021a0, 'exit_020021a0'),
        (0x20021b0, 'fwrite_020021b0'),
        (0x20021c0, '__fprintf_chk_020021c0'),
        (0x20021f0, '__ctype_b_loc_020021f0'),
        (0x2002200, 'free_02002200'),
        (0x2002208, '__cxa_finalize_02002208'),
        (0x2002210, 'chown.main'),
        (0x20027a0, 'chown.__entry'),
        (0x2002860, 'chown.fini_function_0'),
        (0x20028a0, 'chown.init_function_0'),
        (0x2008420, 'chown.fts_open'),
        (0x20087c0, 'chown.fts_close'),
        (0x2008950, 'chown.fts_read'),
        (0x20090d0, 'chown.fts_set'),
        (0x2009100, 'chown.fts_children'),
        (0x200b08c, 'chown.fini_function'),
        (0x200b0a0, 'chown._IO_stdin_used'),
        (0x200b0a4, 'str_chown_0200b0a4'),
        (0x200b0ac, 'str_test invocation_0200b0ac'),
        (0x200b0bc, 'str_Multi-call invoc_0200b0bc'),
        (0x200b0d2, 'str_sha224sum_0200b0d2'),
        (0x200b0dc, 'str_sha2 utilities_0200b0dc'),
        (0x200b0eb, 'str_sha256sum_0200b0eb'),
        (0x200b0f5, 'str_sha384sum_0200b0f5'),
        (0x200b0ff, 'str_sha512sum_0200b0ff'),
        (0x200b109, 'str_%s online help: _0200b109'),
        (0x200b120, 'str_GNU coreutils_0200b120'),
        (0x200b132, 'str_/usr/share/local_0200b132'),
        (0x200b144, 'str_%s: %s_0200b144'),
        (0x200b14b, 'str_Jim Meyering_0200b14b'),
        (0x200b158, 'str_David MacKenzie_0200b158'),
        (0x200b168, 'str_HLPRcfhv_0200b168'),
        (0x200b171, 'str_missing operand_0200b171'),
        (0x200b181, 'str_missing operand _0200b181'),
        (0x200b19a, 'str_recursive_0200b19a'),
        (0x200b1a4, 'str_changes_0200b1a4'),
        (0x200b1ac, 'str_from_0200b1ac'),
        (0x200b1b1, 'str_no-dereference_0200b1b1'),
        (0x200b1c0, 'str_no-preserve-root_0200b1c0'),
        (0x200b1d1, 'str_quiet_0200b1d1'),
        (0x200b1d7, 'str_silent_0200b1d7'),
        (0x200b1de, 'str_verbose_0200b1de'),
        (0x200b1e6, 'str_help_0200b1e6'),
        (0x200b1eb, 'str_version_0200b1eb'),
        (0x200b1f8, "str_Try '%s --help' _0200b1f8"),
        (0x200b220, 'str_Usage: %s [OPTIO_0200b220'),
        (0x200b288, 'str_Change the owner_0200b288'),
        (0x200b320, 'str_  -c, --changes _0200b320'),
        (0x200b3f0, 'str_      --derefere_0200b3f0'),
        (0x200b4d8, 'str_                _0200b4d8'),
        (0x200b550, 'str_      --from=CUR_0200b550'),
        (0x200b6a8, 'str_      --no-prese_0200b6a8'),
        (0x200b728, 'str_      --referenc_0200b728'),
        (0x200b7a8, 'str_  -R, --recursiv_0200b7a8'),
        (0x200b7f0, 'str_The following op_0200b7f0'),
        (0x200b9c8, 'str_      --help    _0200b9c8'),
        (0x200b9f8, 'str_      --version _0200b9f8'),
        (0x200ba30, 'str_Owner is unchang_0200ba30'),
        (0x200baf0, 'str_Examples:  %s ro_0200baf0'),
        (0x200bbc0, 'str_http://www.gnu.o_0200bbc0'),
        (0x200bbe8, 'str_Report %s transl_0200bbe8'),
        (0x200bc30, 'str_Full documentati_0200bc30'),
        (0x200bc50, 'str_or available loc_0200bc50'),
        (0x200bc88, 'str_-R --dereference_0200bc88'),
        (0x200bcb8, 'str_failed to get at_0200bcb8'),
        (0x200bd01, 'str_cannot dereferen_0200bd01'),
        (0x200bd17, 'str_changing ownersh_0200bd17'),
        (0x200bd30, 'str_changing group o_0200bd30'),
        (0x200bd45, 'str_no change to own_0200bd45'),
        (0x200bd63, 'str_group of %s reta_0200bd63'),
        (0x200bd7f, 'str_ownership of %s _0200bd7f'),
        (0x200bd99, 'str_fts_read failed_0200bd99'),
        (0x200bda9, 'str_fts_close failed_0200bda9'),
        (0x200bdc0, 'str_it is dangerous _0200bdc0'),
        (0x200bdf0, 'str_it is dangerous _0200bdf0'),
        (0x200be30, 'str_use --no-preserv_0200be30'),
        (0x200bf28, 'str_changed ownershi_0200bf28'),
        (0x200bf50, 'str_changed group of_0200bf50'),
        (0x200bf78, 'str_failed to change_0200bf78'),
        (0x200bfa8, 'str_failed to change_0200bfa8'),
        (0x200bfd8, 'str_failed to change_0200bfd8'),
        (0x200c000, 'str_failed to change_0200c000'),
        (0x200c028, 'str_failed to change_0200c028'),
        (0x200c050, 'str_ownership of %s _0200c050'),
        (0x200c070, 'str_neither symbolic_0200c070'),
        (0x200c0d4, 'str_8.28_0200c0d4'),
        (0x200c0d9, 'str_write error_0200c0d9'),
        (0x200c0e8, 'str_A NULL argv[0] w_0200c0e8'),
        (0x200c120, 'str_/.libs/_0200c120'),
        (0x200c141, 'str_literal_0200c141'),
        (0x200c149, 'str_shell_0200c149'),
        (0x200c14f, 'str_shell-always_0200c14f'),
        (0x200c15c, 'str_shell-escape_0200c15c'),
        (0x200c169, 'str_shell-escape-alw_0200c169'),
        (0x200c17d, 'str_c-maybe_0200c17d'),
        (0x200c185, 'str_clocale_0200c185'),
        (0x200c5e0, 'chown.quoting_style_vals'),
        (0x200c608, 'str_invalid user_0200c608'),
        (0x200c615, 'str_invalid spec_0200c615'),
        (0x200c622, 'str_invalid group_0200c622'),
        (0x200c630, 'str_%s (%s) %s_0200c630'),
        (0x200c63c, 'str_%s %s_0200c63c'),
        (0x200c6d0, 'str_License GPLv3+: _0200c6d0'),
        (0x200c8a8, 'str_Written by %s, %_0200c8a8'),
        (0x200c960, 'chown.version_etc_copyright'),
        (0x200c98f, 'str_memory exhausted_0200c98f'),
        (0x200c9a0, 'str_lib/xfts.c_0200c9a0'),
        (0x200c9ab, 'str_errno != EINVAL_0200c9ab'),
        (0x200c9c0, 'str_xfts_open_0200c9c0'),
        (0x200c9ca, 'str_lib/xstrtol.c_0200c9ca'),
        (0x200c9d8, 'str_0 <= strtol_base_0200c9d8'),
        (0x200cad8, 'str_xstrtoul_0200cad8'),
        (0x200cb30, 'str_lib/cycle-check._0200cb30'),
        (0x200cb42, 'str_state->magic == _0200cb42'),
        (0x200cb60, 'str_cycle_check_0200cb60'),
        (0x200cb6e, 'str_POSIX_0200cb6e'),
        (0x200cc30, 'str_ASCII_0200cc30'),
        (0x200cc36, 'str_/usr/lib/x86_64-_0200cc36'),
        (0x200cc50, 'str_CHARSETALIASDIR_0200cc50'),
        (0x200cc60, 'str_%50s %50s_0200cc60'),
        (0x220fb20, 'chown.quoting_style_args'),
        (0x220fd80, '*.endgrent_0220fd80'),
        (0x220fd88, '*.__uflow_0220fd88'),
        (0x220fd90, '*.getenv_0220fd90'),
        (0x220fd98, '*.abort_0220fd98'),
        (0x220fda0, '*.__errno_location_0220fda0'),
        (0x220fda8, '*.strncmp_0220fda8'),
        (0x220fdb0, '*._exit_0220fdb0'),
        (0x220fdb8, '*.strcpy_0220fdb8'),
        (0x220fdc0, '*.__fpending_0220fdc0'),
        (0x220fdc8, '*.qsort_0220fdc8'),
        (0x220fdd0, '*.fcntl_0220fdd0'),
        (0x220fdd8, '*.textdomain_0220fdd8'),
        (0x220fde0, '*.fclose_0220fde0'),
        (0x220fde8, '*.getpwuid_0220fde8'),
        (0x220fdf0, '*.bindtextdomain_0220fdf0'),
        (0x220fdf8, '*.stpcpy_0220fdf8'),
        (0x220fe00, '*.dcgettext_0220fe00'),
        (0x220fe08, '*.__ctype_get_mb_cur_max_0220fe08'),
        (0x220fe10, '*.strlen_0220fe10'),
        (0x220fe18, '*.__lxstat_0220fe18'),
        (0x220fe20, '*.openat_0220fe20'),
        (0x220fe28, '*.__stack_chk_fail_0220fe28'),
        (0x220fe30, '*.getopt_long_0220fe30'),
        (0x220fe38, '*.mbrtowc_0220fe38'),
        (0x220fe40, '*.strchr_0220fe40'),
        (0x220fe48, '*.getgrgid_0220fe48'),
        (0x220fe50, '*.__fxstatat_0220fe50'),
        (0x220fe58, '*.strrchr_0220fe58'),
        (0x220fe60, '*.lseek_0220fe60'),
        (0x220fe68, '*.__assert_fail_0220fe68'),
        (0x220fe70, '*.memset_0220fe70'),
        (0x220fe78, '*.fscanf_0220fe78'),
        (0x220fe80, '*.close_0220fe80'),
        (0x220fe88, '*.__openat_2_0220fe88'),
        (0x220fe90, '*.closedir_0220fe90'),
        (0x220fe98, '*.memcmp_0220fe98'),
        (0x220fea0, '*.fputs_unlocked_0220fea0'),
        (0x220fea8, '*.calloc_0220fea8'),
        (0x220feb0, '*.strcmp_0220feb0'),
        (0x220feb8, '*.dirfd_0220feb8'),
        (0x220fec0, '*.getpwnam_0220fec0'),
        (0x220fec8, '*.memcpy_0220fec8'),
        (0x220fed0, '*.getgrnam_0220fed0'),
        (0x220fed8, '*.fileno_0220fed8'),
        (0x220fee0, '*.__xstat_0220fee0'),
        (0x220fee8, '*.readdir_0220fee8'),
        (0x220fef0, '*.malloc_0220fef0'),
        (0x220fef8, '*.fflush_0220fef8'),
        (0x220ff00, '*.nl_langinfo_0220ff00'),
        (0x220ff08, '*.ungetc_0220ff08'),
        (0x220ff10, '*.__fxstat_0220ff10'),
        (0x220ff18, '*.endpwent_0220ff18'),
        (0x220ff20, '*.__freading_0220ff20'),
        (0x220ff28, '*.fchdir_0220ff28'),
        (0x220ff30, '*.realloc_0220ff30'),
        (0x220ff38, '*.fdopen_0220ff38'),
        (0x220ff40, '*.setlocale_0220ff40'),
        (0x220ff48, '*.__printf_chk_0220ff48'),
        (0x220ff50, '*.memmove_0220ff50'),
        (0x220ff58, '*.error_0220ff58'),
        (0x220ff60, '*.open_0220ff60'),
        (0x220ff68, '*.fseeko_0220ff68'),
        (0x220ff70, '*.fchown_0220ff70'),
        (0x220ff78, '*.fdopendir_0220ff78'),
        (0x220ff80, '*.strtoul_0220ff80'),
        (0x220ff88, '*.fstatfs_0220ff88'),
        (0x220ff90, '*.__cxa_atexit_0220ff90'),
        (0x220ff98, '*.fchownat_0220ff98'),
        (0x220ffa0, '*.exit_0220ffa0'),
        (0x220ffa8, '*.fwrite_0220ffa8'),
        (0x220ffb0, '*.__fprintf_chk_0220ffb0'),
        (0x220ffb8, '*.mbsinit_0220ffb8'),
        (0x220ffc0, '*.iswprint_0220ffc0'),
        (0x220ffc8, '*.__ctype_b_loc_0220ffc8'),
        (0x220ffd0, '*.free_0220ffd0'),
        (0x220ffd8, '*._ITM_deregisterTMCloneTable_0220ffd8'),
        (0x220ffe0, '*.__libc_start_main_0220ffe0'),
        (0x220ffe8, '*.__gmon_start___0220ffe8'),
        (0x220fff0, '*._ITM_registerTMCloneTable_0220fff0'),
        (0x220fff8, '*.__cxa_finalize_0220fff8'),
        (0x2210010, 'chown.Version'),
        (0x2210018, 'chown.exit_failure'),
        (0x2210020, 'chown.quote_quoting_options'),
        (0x2210080, 'chown.program_invocation_short_name'),
        (0x2210088, 'chown.stdout'),
        (0x2210090, 'chown.optind'),
        (0x22100a0, 'chown.optarg'),
        (0x22100a8, 'chown.__progname_full'),
        (0x22100c0, 'chown.stderr'),
        (0x22100f8, 'chown.program_name'),
        (0x6572006b6a635f66, 'chown.'),
    ],

    'pltgot' : [
    ],

}


