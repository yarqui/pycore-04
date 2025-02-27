def get_cats_info(path: str) -> list:
    try:
        if not isinstance(path, str):
            raise TypeError('Path should be a string')
        
        with open(path, encoding='UTF-8') as fh:
            return [
                {'id': cat[0], 'name': cat[1], 'age': cat[2]}
                for line in fh
                if (cat := line.strip().split(',')) and len(cat) == 3
            ]

    except Exception as err:
        print(f'{type(err)}: {err}')
        return []
    
print(get_cats_info('cats.txt'))