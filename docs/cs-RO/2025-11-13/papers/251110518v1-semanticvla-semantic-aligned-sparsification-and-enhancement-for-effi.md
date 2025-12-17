---
layout: default
title: SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation
---

# SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation

**arXiv**: [2511.10518v1](https://arxiv.org/abs/2511.10518) | [PDF](https://arxiv.org/pdf/2511.10518.pdf)

**作者**: Wei Li, Renshan Zhang, Rui Shao, Zhijian Fang, Kaiwen Zhou, Zhuotao Tian, Liqiang Nie

---

## 💡 一句话要点

**提出SemanticVLA框架，通过语义对齐稀疏化与增强提升机器人操作效率**

**关键词**: `机器人操作` `视觉-语言-动作模型` `语义对齐` `稀疏化` `特征融合` `高效推理`

## 📋 核心要点

1. 核心问题：视觉-语言-动作模型存在感知冗余和指令-视觉对齐不足，影响机器人操作效率
2. 方法要点：使用语义引导双视觉剪枝器和分层融合器，稀疏化视觉输入并融合语义与几何特征
3. 实验或效果：在LIBERO基准上成功率提升21.1%，训练和推理成本分别降低3.0倍和2.7倍

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have advanced in robotic manipulation, yet practical deployment remains hindered by two key limitations: 1) perceptual redundancy, where irrelevant visual inputs are processed inefficiently, and 2) superficial instruction-vision alignment, which hampers semantic grounding of actions. In this paper, we propose SemanticVLA, a novel VLA framework that performs Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation. Specifically: 1) To sparsify redundant perception while preserving semantic alignment, Semantic-guided Dual Visual Pruner (SD-Pruner) performs: Instruction-driven Pruner (ID-Pruner) extracts global action cues and local semantic anchors in SigLIP; Spatial-aggregation Pruner (SA-Pruner) compacts geometry-rich features into task-adaptive tokens in DINOv2. 2) To exploit sparsified features and integrate semantics with spatial geometry, Semantic-complementary Hierarchical Fuser (SH-Fuser) fuses dense patches and sparse tokens across SigLIP and DINOv2 for coherent representation. 3) To enhance the transformation from perception to action, Semantic-conditioned Action Coupler (SA-Coupler) replaces the conventional observation-to-DoF approach, yielding more efficient and interpretable behavior modeling for manipulation tasks. Extensive experiments on simulation and real-world tasks show that SemanticVLA sets a new SOTA in both performance and efficiency. SemanticVLA surpasses OpenVLA on LIBERO benchmark by 21.1% in success rate, while reducing training cost and inference latency by 3.0-fold and 2.7-fold.SemanticVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/SemanticVLA

