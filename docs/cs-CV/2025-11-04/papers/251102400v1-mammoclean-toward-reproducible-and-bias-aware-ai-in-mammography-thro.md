---
layout: default
title: MammoClean: Toward Reproducible and Bias-Aware AI in Mammography through Dataset Harmonization
---

# MammoClean: Toward Reproducible and Bias-Aware AI in Mammography through Dataset Harmonization

**arXiv**: [2511.02400v1](https://arxiv.org/abs/2511.02400) | [PDF](https://arxiv.org/pdf/2511.02400.pdf)

**作者**: Yalda Zafari, Hongyi Pan, Gorkem Durak, Ulas Bagci, Essam A. Rashed, Mohamed Mabrok

---

## 💡 一句话要点

**提出MammoClean框架以解决乳腺X光数据异质性导致的AI模型泛化问题**

**关键词**: `乳腺X光影像` `数据集标准化` `偏差量化` `AI泛化性` `多数据集训练` `开源框架`

## 📋 核心要点

1. 乳腺X光数据存在质量和分布异质性，导致AI模型泛化性差
2. MammoClean标准化数据选择、图像处理和元数据，统一多视图结构
3. 应用框架量化数据集偏差，提升模型跨域性能，代码开源可用

## 📄 摘要（原文）

> The development of clinically reliable artificial intelligence (AI) systems
> for mammography is hindered by profound heterogeneity in data quality, metadata
> standards, and population distributions across public datasets. This
> heterogeneity introduces dataset-specific biases that severely compromise the
> generalizability of the model, a fundamental barrier to clinical deployment. We
> present MammoClean, a public framework for standardization and bias
> quantification in mammography datasets. MammoClean standardizes case selection,
> image processing (including laterality and intensity correction), and unifies
> metadata into a consistent multi-view structure. We provide a comprehensive
> review of breast anatomy, imaging characteristics, and public mammography
> datasets to systematically identify key sources of bias. Applying MammoClean to
> three heterogeneous datasets (CBIS-DDSM, TOMPEI-CMMD, VinDr-Mammo), we quantify
> substantial distributional shifts in breast density and abnormality prevalence.
> Critically, we demonstrate the direct impact of data corruption: AI models
> trained on corrupted datasets exhibit significant performance degradation
> compared to their curated counterparts. By using MammoClean to identify and
> mitigate bias sources, researchers can construct unified multi-dataset training
> corpora that enable development of robust models with superior cross-domain
> generalization. MammoClean provides an essential, reproducible pipeline for
> bias-aware AI development in mammography, facilitating fairer comparisons and
> advancing the creation of safe, effective systems that perform equitably across
> diverse patient populations and clinical settings. The open-source code is
> publicly available from: https://github.com/Minds-R-Lab/MammoClean.

