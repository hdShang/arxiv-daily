---
layout: default
title: QuantumCanvas: A Multimodal Benchmark for Visual Learning of Atomic Interactions
---

# QuantumCanvas: A Multimodal Benchmark for Visual Learning of Atomic Interactions

**arXiv**: [2512.01519v1](https://arxiv.org/abs/2512.01519) | [PDF](https://arxiv.org/pdf/2512.01519.pdf)

**作者**: Can Polat, Erchin Serpedin, Mustafa Kurban, Hasan Kurban

---

## 💡 一句话要点

**提出QuantumCanvas多模态基准，通过视觉表示学习原子间量子相互作用以提升物理可迁移性。**

**关键词**: `量子相互作用学习` `多模态基准` `视觉表示学习` `原子对建模` `物理可迁移性` `轨道密度图像`

## 📋 核心要点

1. 核心问题：现有分子与材料机器学习模型缺乏物理可迁移性，未学习原子对间的量子相互作用。
2. 方法要点：构建大规模多模态基准，包含元素对的多属性标注和基于轨道密度等的十通道图像表示。
3. 实验或效果：基准测试显示模型在能量相关量上表现优异，预训练提升在QM9等数据集上的泛化能力。

## 📄 摘要（原文）

> Despite rapid advances in molecular and materials machine learning, most models still lack physical transferability: they fit correlations across whole molecules or crystals rather than learning the quantum interactions between atomic pairs. Yet bonding, charge redistribution, orbital hybridization, and electronic coupling all emerge from these two-body interactions that define local quantum fields in many-body systems. We introduce QuantumCanvas, a large-scale multimodal benchmark that treats two-body quantum systems as foundational units of matter. The dataset spans 2,850 element-element pairs, each annotated with 18 electronic, thermodynamic, and geometric properties and paired with ten-channel image representations derived from l- and m-resolved orbital densities, angular field transforms, co-occupancy maps, and charge-density projections. These physically grounded images encode spatial, angular, and electrostatic symmetries without explicit coordinates, providing an interpretable visual modality for quantum learning. Benchmarking eight architectures across 18 targets, we report mean absolute errors of 0.201 eV on energy gap using GATv2, 0.265 eV on HOMO and 0.274 eV on LUMO using EGNN. For energy-related quantities, DimeNet attains 2.27 eV total-energy MAE and 0.132 eV repulsive-energy MAE, while a multimodal fusion model achieves a 2.15 eV Mermin free-energy MAE. Pretraining on QuantumCanvas further improves convergence stability and generalization when fine-tuned on larger datasets such as QM9, MD17, and CrysMTM. By unifying orbital physics with vision-based representation learning, QuantumCanvas provides a principled and interpretable basis for learning transferable quantum interactions through coupled visual and numerical modalities. Dataset and model implementations are available at https://github.com/KurbanIntelligenceLab/QuantumCanvas.

