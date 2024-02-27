select concat("/home/grep/src/", b.board_id, "/", f.file_id, f.file_name, f.file_ext) as 'FILE_PATH' from used_goods_board as b, used_goods_file as f
where b.board_id = f.board_id and b.views = (select max(views) from used_goods_board)
order by file_id desc