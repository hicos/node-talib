{
    'targets': [
        {
            'target_name': 'talib',
            'sources': [
                'src/talib.cpp'
            ],
            'link_settings': {
                'libraries': [
                    '../src/lib/lib/libta_libc_csr.a'
                ]
            }
        }
    ]
}