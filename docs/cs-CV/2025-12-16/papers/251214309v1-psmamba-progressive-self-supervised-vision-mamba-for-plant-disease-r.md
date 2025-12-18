---
layout: default
title: PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
---

# PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14309" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14309v1</a>
  <a href="https://arxiv.org/pdf/2512.14309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14309v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14309v1', 'PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**PSMamba：一种用于植物病害识别的渐进式自监督视觉Mamba框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `植物病害识别` `自监督学习` `Vision Mamba` `分层蒸馏` `双学生网络` `多尺度特征` `领域泛化` `计算机视觉`

## 📋 核心要点

1. 现有自监督学习方法难以有效捕捉植物病害图像中复杂的分层、多尺度病变特征。
2. PSMamba通过双学生分层蒸馏策略，结合全局和局部视图，实现上下文和细节表征的联合学习。
3. 实验结果表明，PSMamba在植物病害识别任务中，显著优于现有自监督学习方法，尤其是在领域泛化和细粒度识别方面。

## 📝 摘要（中文）

自监督学习(SSL)已成为一种无需手动标注即可进行表征学习的强大范例。然而，现有的大多数框架侧重于全局对齐，难以捕捉植物病害图像中具有代表性的分层、多尺度病变模式。为了解决这一差距，我们提出了PSMamba，一个渐进式自监督框架，它将Vision Mamba (VM)的高效序列建模与双学生分层蒸馏策略相结合。与传统的单教师-学生设计不同，PSMamba采用共享的全局教师和两个专门的学生：一个处理中等尺度的视图以捕获病变分布和静脉结构，而另一个侧重于局部视图以捕获细粒度的线索，如纹理不规则和早期病变。这种多粒度监督促进了上下文和详细表征的联合学习，一致性损失确保了连贯的跨尺度对齐。在三个基准数据集上的实验表明，PSMamba始终优于最先进的SSL方法，在领域转移和细粒度场景中均提供了卓越的准确性和鲁棒性。

## 🔬 方法详解

**问题定义**：植物病害识别需要捕捉病变的分层、多尺度特征，但现有自监督学习方法侧重于全局对齐，忽略了局部细节和不同尺度的信息，导致识别精度受限。现有方法难以有效处理领域迁移带来的挑战，鲁棒性不足。

**核心思路**：PSMamba的核心在于利用双学生网络，分别学习不同尺度的特征表示。一个学生关注中等尺度的病变分布和静脉结构，另一个学生关注局部视图的纹理不规则和早期病变。通过分层蒸馏和一致性损失，将两个学生学习到的特征进行融合，从而获得更全面、更鲁棒的表征。

**技术框架**：PSMamba包含一个共享的全局教师网络和两个专门的学生网络。教师网络提供全局上下文信息，两个学生网络分别处理中等尺度和局部尺度的视图。通过分层蒸馏，学生网络学习教师网络的知识，并通过一致性损失确保跨尺度特征的一致性。最终，将两个学生网络的特征进行融合，用于植物病害识别。

**关键创新**：PSMamba的关键创新在于双学生分层蒸馏策略，它能够同时捕捉全局上下文信息和局部细节信息，从而更有效地学习植物病害图像的特征表示。此外，PSMamba将Vision Mamba (VM)的高效序列建模能力引入自监督学习框架，提高了模型的效率和性能。

**关键设计**：PSMamba使用Vision Mamba作为骨干网络，利用其高效的序列建模能力。损失函数包括分层蒸馏损失和一致性损失，用于指导学生网络的学习和确保跨尺度特征的一致性。具体的参数设置和网络结构细节在论文中有详细描述，例如不同尺度视图的采样策略、损失函数的权重等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/global.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/psmamba.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/visual/gradcam/pd_o_2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PSMamba在三个基准数据集上取得了显著的性能提升，超越了现有的自监督学习方法。实验结果表明，PSMamba在领域转移和细粒度场景中均表现出卓越的准确性和鲁棒性。具体的性能数据和对比基线在论文中有详细展示，例如在某个数据集上，PSMamba的准确率比最先进的方法提高了X%。

## 🎯 应用场景

PSMamba在植物病害识别领域具有广泛的应用前景，可用于农业生产中的病害早期检测、精准防治和智能化管理。该研究成果有助于提高农作物产量和质量，减少农药使用，促进农业可持续发展。未来，该方法可扩展到其他图像识别任务，例如医学图像分析、遥感图像解译等。

## 📄 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

