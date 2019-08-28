# docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/stream_dimensionreduction python /stream/dimred_command_line.py -m $PWD/test/data/bar_stream_result.pkl -of gup_  --flag_savefig -nb_pct 0.1 -method 'mlle' -feat 'var_genes' -n_comp_k 3 -nc_plot 3 -comp1 0 -comp2 1 -fig_name foofoo -fig_width 10 -fig_height 7 -fig_legend_ncol 3


#docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/stream_dimensionreduction python /stream/dimred_command_line.py -m $PWD/test/data/bar_stream_result.pkl -of gup_ -nb_pct 0.1 -n_comp_k 3 -feat 'var_genes' -method 'mlle'  -nc_plot 3 -comp1 0 -comp2 1  --flag_savefig  -fig_name foofoo.pdf -fig_width 10 -fig_height 7 -fig_legend_ncol 3

docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/stream_dimensionreduction python /stream/dimred_command_line.py -m  $PWD/test/data/bar_stream_result.pkl   -of foo -nb_pct .1 -n_comp_k 3 -feat var_genes -method mlle -nc_plot 3 -comp1 0 -comp2 1 --flag_savefig -fig_width 8 -fig_height 8 -fig_name foo_dimensionreduction.pdf -fig_legend_ncol 3

# FAILS
#docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/stream_dimensionreduction python /stream/dimred_command_line.py -m $PWD/test/data/bar_stream_result.pkl  -of foo -nb_pct .1 -n_comp_k 3 -feat var_genes -method mlle -nc_plot 2 -comp1 0 -comp2 1 --flag_savefig -fig_width 8 -fig_height 8 -fig_name foo_dimensionreduction.pdf -fig_legend_ncol 3

