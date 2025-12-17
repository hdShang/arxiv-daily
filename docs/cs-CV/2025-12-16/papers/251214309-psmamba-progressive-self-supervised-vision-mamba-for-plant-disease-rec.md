---
layout: default
title: PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
---

# PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14309" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14309</a>
  <a href="https://arxiv.org/pdf/2512.14309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14309" onclick="toggleFavorite(this, '2512.14309', 'PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**PSMamba：一种用于植物病害识别的渐进式自监督视觉Mamba框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `植物病害识别` `自监督学习` `Vision Mamba` `分层蒸馏` `双学生网络` `多尺度特征` `一致性学习` `计算机视觉`

## 📋 核心要点

1. 现有自监督学习方法难以有效捕捉植物病害图像中复杂的分层、多尺度病变特征。
2. PSMamba采用双学生分层蒸馏策略，结合全局教师和两个分别关注中尺度和局部尺度的学生网络。
3. 实验结果表明，PSMamba在植物病害识别任务中，显著优于现有自监督学习方法，具有更好的准确性和鲁棒性。

## 📝 摘要（中文）

自监督学习(SSL)已成为一种无需手动标注即可进行表征学习的强大范例。然而，现有的大多数框架侧重于全局对齐，难以捕捉植物病害图像中具有代表性的分层、多尺度病变模式。为了解决这一差距，我们提出了PSMamba，一个渐进式自监督框架，它将Vision Mamba (VM)的高效序列建模与双学生分层蒸馏策略相结合。与传统的单教师-学生设计不同，PSMamba采用共享的全局教师和两个专门的学生：一个处理中等尺度的视图以捕捉病变分布和静脉结构，而另一个则侧重于局部视图以捕捉纹理不规则和早期病变等细粒度线索。这种多粒度监督促进了上下文和详细表征的联合学习，一致性损失确保了连贯的跨尺度对齐。在三个基准数据集上的实验表明，PSMamba始终优于最先进的SSL方法，在领域迁移和细粒度场景中均提供了卓越的准确性和鲁棒性。

## 🔬 方法详解

**问题定义**：植物病害识别依赖于对病变区域的准确表征。现有自监督学习方法侧重于全局特征对齐，忽略了病害图像中重要的分层、多尺度局部病变信息，导致识别精度受限。

**核心思路**：PSMamba的核心在于通过渐进式的自监督学习，利用双学生网络分别学习不同尺度的病变特征，并利用一致性损失保证跨尺度特征的一致性。这种方法旨在弥补现有方法在捕捉局部细节和多尺度信息方面的不足。

**技术框架**：PSMamba框架包含一个共享的全局教师网络和两个专门的学生网络。全局教师网络学习全局图像表征。一个学生网络专注于中等尺度的视图，捕捉病变分布和静脉结构；另一个学生网络专注于局部视图，捕捉纹理不规则和早期病变等细粒度线索。通过分层蒸馏和一致性损失，学生网络学习教师网络的知识，并相互对齐。

**关键创新**：PSMamba的关键创新在于其双学生分层蒸馏策略，该策略允许模型同时学习全局上下文信息和局部细节信息。此外，PSMamba利用Vision Mamba (VM)作为骨干网络，提高了序列建模的效率。

**关键设计**：PSMamba使用Vision Mamba作为骨干网络，利用其高效的序列建模能力。双学生网络分别处理不同尺度的图像视图。一致性损失用于约束两个学生网络输出的一致性，确保跨尺度特征对齐。具体的损失函数选择和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309/Figures/global.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309/Figures/psmamba.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309/Figures/visual/gradcam/pd_o_2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PSMamba在三个基准植物病害数据集上进行了评估，实验结果表明，PSMamba consistently outperforms state-of-the-art SSL methods，在领域迁移和细粒度场景中均提供了卓越的准确性和鲁棒性。具体性能提升数据需要在论文中查找。

## 🎯 应用场景

PSMamba在植物病害识别领域具有广泛的应用前景，可以帮助农民和农业专家快速准确地诊断植物病害，从而采取及时的防治措施，减少作物损失，提高农业生产效率。该方法还可以扩展到其他医学图像分析、遥感图像分析等领域，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

