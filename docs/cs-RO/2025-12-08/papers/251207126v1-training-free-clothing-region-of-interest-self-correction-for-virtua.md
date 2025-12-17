---
layout: default
title: Training-free Clothing Region of Interest Self-correction for Virtual Try-On
---

# Training-free Clothing Region of Interest Self-correction for Virtual Try-On

**arXiv**: [2512.07126v1](https://arxiv.org/abs/2512.07126) | [PDF](https://arxiv.org/pdf/2512.07126.pdf)

**作者**: Shengjie Lu, Zhibin Wan, Jiejie Liu, Quan Zhang, Mingjie Sun

---

## 💡 一句话要点

**提出无训练服装感兴趣区域自校正方法以提升虚拟试穿效果**

**关键词**: `虚拟试穿` `注意力机制` `能量函数` `评估指标` `服装区域校正` `生成对抗网络`

## 📋 核心要点

1. 现有虚拟试穿方法在图案、纹理和边界上存在生成服装与目标服装的差异问题
2. 通过能量函数约束生成过程中的注意力图，使注意力更集中于服装区域，改善细节一致性
3. 在VITON-HD和DressCode数据集上，传统指标和新VTID指标均优于先前方法，并提升下游任务性能

## 📄 摘要（原文）

> VTON (Virtual Try-ON) aims at synthesizing the target clothing on a certain person, preserving the details of the target clothing while keeping the rest of the person unchanged. Existing methods suffer from the discrepancies between the generated clothing results and the target ones, in terms of the patterns, textures and boundaries. Therefore, we propose to use an energy function to impose constraints on the attention map extracted through the generation process. Thus, at each generation step, the attention can be more focused on the clothing region of interest, thereby influencing the generation results to be more consistent with the target clothing details. Furthermore, to address the limitation that existing evaluation metrics concentrate solely on image realism and overlook the alignment with target elements, we design a new metric, Virtual Try-on Inception Distance (VTID), to bridge this gap and ensure a more comprehensive assessment. On the VITON-HD and DressCode datasets, our approach has outperformed the previous state-of-the-art (SOTA) methods by 1.4%, 2.3%, 12.3%, and 5.8% in the traditional metrics of LPIPS, FID, KID, and the new VTID metrics, respectively. Additionally, by applying the generated data to downstream Clothing-Change Re-identification (CC-Reid) methods, we have achieved performance improvements of 2.5%, 1.1%, and 1.6% on the LTCC, PRCC, VC-Clothes datasets in the metrics of Rank-1. The code of our method is public at https://github.com/MrWhiteSmall/CSC-VTON.git.

