FROM continuumio/miniconda3

WORKDIR /src/cf2cdm

COPY environment.yml /src/cf2cdm/

RUN conda install -c conda-forge gcc python=3.10 \
    && conda env update -n base -f environment.yml

COPY . /src/cf2cdm

RUN pip install --no-deps -e .
