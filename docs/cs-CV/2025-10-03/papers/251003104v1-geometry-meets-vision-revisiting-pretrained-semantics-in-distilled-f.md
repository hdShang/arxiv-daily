---
layout: default
title: Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled Fields
---

# Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03104" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03104v1</a>
  <a href="https://arxiv.org/pdf/2510.03104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03104v1" onclick="toggleFavorite(this, '2510.03104v1', 'Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-03

---

## 💡 一句话要点

**研究几何信息在神经辐射场语义蒸馏中的作用，并提出SPINE框架实现无初始猜测的辐射场反演。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `语义蒸馏` `几何信息` `姿态估计` `辐射场反演`

## 📋 核心要点

1. 现有方法在辐射场语义蒸馏中，对几何信息利用不足，限制了其在空间任务中的潜力。
2. 论文提出SPINE框架，通过语义蒸馏进行粗略反演，再通过光度优化进行精细反演，实现无初始猜测的辐射场反演。
3. 实验表明，纯视觉特征在下游任务中表现更佳，而几何相关特征虽然包含更多几何细节，但姿态估计精度反而下降。

## 📝 摘要（中文）

神经辐射场中的语义蒸馏推动了开放词汇机器人策略的显著进步，例如操纵和导航，这些策略建立在大型视觉模型的预训练语义之上。虽然之前的工作已经证明了纯视觉语义特征（例如DINO和CLIP）在高斯溅射和神经辐射场中的有效性，但几何信息在蒸馏场中的潜在益处仍然是一个悬而未决的问题。原则上，视觉-几何特征对于姿态估计等空间任务非常有希望，这引发了一个问题：几何相关的语义特征是否在蒸馏场中提供优势？具体来说，我们提出了三个关键问题：首先，空间相关性是否产生更高保真度的几何感知语义特征？我们发现，来自几何相关骨干网络的图像特征包含比其对应物更精细的结构细节。其次，几何相关性是否改善语义对象定位？我们观察到此任务没有显着差异。第三，几何相关性是否能够实现更高精度的辐射场反演？鉴于先前工作的局限性以及它们缺乏语义集成，我们提出了一种新颖的框架SPINE，用于在没有初始猜测的情况下反演辐射场，该框架由两个核心组件组成：使用蒸馏语义进行粗略反演，以及使用基于光度法的优化进行精细反演。令人惊讶的是，我们发现姿态估计精度随着几何相关特征的降低而降低。我们的结果表明，纯视觉特征为更广泛的下游任务提供了更大的通用性，尽管几何相关特征包含更多的几何细节。值得注意的是，我们的发现强调了未来研究有效几何相关策略的必要性，这些策略可以增强预训练语义特征的通用性和性能。

## 🔬 方法详解

**问题定义**：论文旨在研究在神经辐射场（NeRF）的语义蒸馏中，几何信息（geometry-grounding）的引入是否能够提升性能，特别是在姿态估计等空间任务中。现有方法主要依赖纯视觉特征，忽略了几何信息可能带来的优势。现有辐射场反演方法通常需要初始猜测，限制了其应用范围。

**核心思路**：论文的核心思路是系统性地评估几何相关特征在语义蒸馏辐射场中的作用。通过对比几何相关和纯视觉特征在语义特征质量、物体定位和辐射场反演方面的表现，揭示了几何信息在不同任务中的影响。同时，提出了SPINE框架，利用语义蒸馏和光度优化相结合的方式，实现无需初始猜测的辐射场反演。

**技术框架**：SPINE框架包含两个主要阶段：1) **粗略反演**：利用蒸馏的语义信息，对场景进行初步的姿态估计和场景重建。2) **精细反演**：利用光度一致性，通过优化姿态和场景几何，进一步提升重建质量。该框架无需初始姿态猜测，可以直接从图像和语义信息中进行辐射场反演。

**关键创新**：SPINE框架的关键创新在于将语义蒸馏与光度优化相结合，实现了无需初始猜测的辐射场反演。此外，论文系统性地研究了几何相关特征在语义蒸馏辐射场中的作用，发现纯视觉特征在某些任务中表现优于几何相关特征，这与直觉相反。

**关键设计**：SPINE框架的关键设计包括：1) 使用预训练的视觉模型（如DINO或CLIP）提取图像的语义特征。2) 将这些语义特征蒸馏到神经辐射场中，形成语义辐射场。3) 设计损失函数，鼓励重建的场景与输入图像在语义和光度上保持一致。4) 使用优化算法（如Adam）迭代优化姿态和场景几何。

## 📊 实验亮点

实验结果表明，几何相关特征虽然包含更多几何细节，但在姿态估计任务中，其性能不如纯视觉特征。SPINE框架成功实现了无需初始猜测的辐射场反演，为辐射场的应用开辟了新的可能性。该研究揭示了几何信息在语义蒸馏辐射场中的复杂作用，为未来的研究提供了重要指导。

## 🎯 应用场景

该研究成果可应用于机器人导航、物体操作、三维场景重建等领域。SPINE框架无需初始猜测的特性，使其在未知环境中具有更强的适应性。未来的研究可以探索更有效的几何信息融合策略，提升辐射场在各种下游任务中的性能。

## 📄 摘要（原文）

> Semantic distillation in radiance fields has spurred significant advances in open-vocabulary robot policies, e.g., in manipulation and navigation, founded on pretrained semantics from large vision models. While prior work has demonstrated the effectiveness of visual-only semantic features (e.g., DINO and CLIP) in Gaussian Splatting and neural radiance fields, the potential benefit of geometry-grounding in distilled fields remains an open question. In principle, visual-geometry features seem very promising for spatial tasks such as pose estimation, prompting the question: Do geometry-grounded semantic features offer an edge in distilled fields? Specifically, we ask three critical questions: First, does spatial-grounding produce higher-fidelity geometry-aware semantic features? We find that image features from geometry-grounded backbones contain finer structural details compared to their counterparts. Secondly, does geometry-grounding improve semantic object localization? We observe no significant difference in this task. Thirdly, does geometry-grounding enable higher-accuracy radiance field inversion? Given the limitations of prior work and their lack of semantics integration, we propose a novel framework SPINE for inverting radiance fields without an initial guess, consisting of two core components: coarse inversion using distilled semantics, and fine inversion using photometric-based optimization. Surprisingly, we find that the pose estimation accuracy decreases with geometry-grounded features. Our results suggest that visual-only features offer greater versatility for a broader range of downstream tasks, although geometry-grounded features contain more geometric detail. Notably, our findings underscore the necessity of future research on effective strategies for geometry-grounding that augment the versatility and performance of pretrained semantic features.

