import Mock from 'mockjs'

Mock.mock(/getnewList/, {
  'list|5': [{
    'url': '@url',
    'title': '@ctitle(5,20)'
  }]
})

Mock.mock(/getproductlist/, {
    pc: {
        title: "PC产品",
        list: [
            {
                title: "@ctitle(5,20)",
                url: "@url"
            },
            {
                title: "@ctitle(5,20)",
                url: "@url"
            },
            {
                title: "@ctitle(5,20)",
                url: "@url",
                hot: '@boolean'
            },
            {
                title: "@ctitle(5,20)",
                url: "@url"
            }
        ]
        },
    app: {
        title: "手机应用类",
        last: '@boolean',
        list: [
            {
                title: "@ctitle(5,20)",
                url: "@url"
            },
            {
                title: "@ctitle(5,20)",
                url: "@url",
                hot: '@boolean'
            },
            {
                title: "@ctitle(5,20)",
                url: "@url"
            },
            {
                title: "@ctitle(5,20)",
                url: "@url",
                hot: '@boolean'
            }
        ]
    }
})

Mock.mock(/getborderlist/,[
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean'
    },
])
export default Mock
