---
layout: default
title: "ATMS-KD: Adaptive Temperature and Mixed Sample Knowledge Distillation for a Lightweight Residual CNN in Agricultural Embedded Systems"
---

# ATMS-KD: Adaptive Temperature and Mixed Sample Knowledge Distillation for a Lightweight Residual CNN in Agricultural Embedded Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20232" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20232v1</a>
  <a href="https://arxiv.org/pdf/2508.20232.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20232v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20232v1', 'ATMS-KD: Adaptive Temperature and Mixed Sample Knowledge Distillation for a Lightweight Residual CNN in Agricultural Embedded Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Ohamouddou, Said Ohamouddou, Abdellatif El Afia, Rafik Lasri

**分类**: cs.CV

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出ATMS-KD框架以提升农业嵌入式系统中的轻量级CNN性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `轻量级CNN` `农业计算机视觉` `自适应温度` `混合样本增强` `嵌入式系统` `模型压缩`

## 📋 核心要点

1. 现有的轻量级CNN模型在资源受限的农业环境中表现不佳，尤其是在知识蒸馏过程中，知识转移效率低。
2. ATMS-KD框架通过自适应温度调度与混合样本增强相结合，提升了知识蒸馏的效果，适应不同容量的学生模型。
3. 实验结果显示，所有学生模型的验证准确率均超过96.7%，且在与其他11种方法对比中，紧凑型模型的准确率提升了1.60个百分点。

## 📝 摘要（中文）

本研究提出了ATMS-KD（自适应温度与混合样本知识蒸馏）框架，旨在开发适合资源受限的农业环境的轻量级CNN模型。该框架结合了自适应温度调度和混合样本增强技术，将知识从MobileNetV3 Large教师模型（5.7M参数）转移到轻量级残差CNN学生模型。实验结果表明，所有学生模型在验证集上的准确率均超过96.7%，显著优于直接训练方法。ATMS-KD框架在11种已知知识蒸馏方法中表现优异，紧凑型模型的准确率达到97.11%，且推理延迟最低为72.19ms，知识保留率超过99%。

## 🔬 方法详解

**问题定义**：本研究旨在解决轻量级CNN模型在农业嵌入式系统中知识蒸馏效率低的问题。现有方法在知识转移过程中，往往无法充分利用教师模型的知识，导致学生模型性能不足。

**核心思路**：ATMS-KD框架通过引入自适应温度调度和混合样本增强，优化了知识蒸馏过程。自适应温度调度可以动态调整知识蒸馏的温度，从而提高学生模型的学习效率，而混合样本增强则通过多样化的输入样本提升模型的泛化能力。

**技术框架**：ATMS-KD框架主要包括两个模块：自适应温度调度模块和混合样本增强模块。首先，教师模型生成软标签，然后通过自适应温度调度调整这些标签的分布，最后将其与混合样本一起输入到学生模型进行训练。

**关键创新**：ATMS-KD的主要创新在于结合了自适应温度调度与混合样本增强，这种设计使得知识蒸馏过程更加高效，显著提高了学生模型的性能，尤其是在参数较少的情况下。

**关键设计**：在参数设置上，学生模型分为紧凑型（1.3M参数）、标准型（2.4M参数）和增强型（3.8M参数），并在损失函数中引入了温度调节因子，以优化知识转移的效果。

## 📊 实验亮点

实验结果显示，ATMS-KD框架在Damascena玫瑰成熟度分类数据集上表现优异，所有学生模型的验证准确率均超过96.7%。紧凑型模型的准确率达到97.11%，比第二名提升了1.60个百分点，同时保持了最低的推理延迟72.19ms，知识保留率超过99%。

## 🎯 应用场景

该研究的ATMS-KD框架具有广泛的应用潜力，特别是在农业计算机视觉领域。通过提升轻量级CNN模型的性能，可以更好地支持农业监测、作物分类和病虫害检测等任务，进而推动智能农业的发展。未来，该框架还可以扩展到其他资源受限的嵌入式系统中，提升其智能化水平。

## 📄 摘要（原文）

> This study proposes ATMS-KD (Adaptive Temperature and Mixed-Sample Knowledge Distillation), a novel framework for developing lightweight CNN models suitable for resource-constrained agricultural environments. The framework combines adaptive temperature scheduling with mixed-sample augmentation to transfer knowledge from a MobileNetV3 Large teacher model (5.7\,M parameters) to lightweight residual CNN students. Three student configurations were evaluated: Compact (1.3\,M parameters), Standard (2.4\,M parameters), and Enhanced (3.8\,M parameters). The dataset used in this study consists of images of \textit{Rosa damascena} (Damask rose) collected from agricultural fields in the Dades Oasis, southeastern Morocco, providing a realistic benchmark for agricultural computer vision applications under diverse environmental conditions. Experimental evaluation on the Damascena rose maturity classification dataset demonstrated significant improvements over direct training methods. All student models achieved validation accuracies exceeding 96.7\% with ATMS-KD compared to 95--96\% with direct training. The framework outperformed eleven established knowledge distillation methods, achieving 97.11\% accuracy with the compact model -- a 1.60 percentage point improvement over the second-best approach while maintaining the lowest inference latency of 72.19\,ms. Knowledge retention rates exceeded 99\% for all configurations, demonstrating effective knowledge transfer regardless of student model capacity.

