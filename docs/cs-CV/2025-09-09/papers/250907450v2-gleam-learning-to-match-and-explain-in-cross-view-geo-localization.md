---
layout: default
title: "GLEAM: Learning to Match and Explain in Cross-View Geo-Localization"
---

# GLEAM: Learning to Match and Explain in Cross-View Geo-Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07450" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07450v2</a>
  <a href="https://arxiv.org/pdf/2509.07450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07450v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07450v2', 'GLEAM: Learning to Match and Explain in Cross-View Geo-Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xudong Lu, Zhi Zheng, Yi Wan, Yongxiang Yao, Annan Wang, Renrui Zhang, Panwang Xia, Qiong Wu, Qingyun Li, Weifeng Lin, Xiangyu Zhao, Peifeng Ma, Xue Yang, Hongsheng Li

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-09 (更新: 2025-09-26)

**备注**: 18 pages

**🔗 代码/项目**: [GITHUB](https://github.com/Lucky-Lance/GLEAM)

---

## 💡 一句话要点

**GLEAM：提出一种多视角地理定位框架，融合匹配与可解释推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨视角地理定位` `多模态融合` `可解释推理` `大型语言模型` `图像匹配`

## 📋 核心要点

1. 现有跨视角地理定位方法局限于单一视角或模态，且缺乏可解释性，无法解释匹配原因。
2. GLEAM框架通过将多种视角和模态（如无人机、街景、全景图等）与卫星图像对齐，实现统一。
3. GLEAM-X任务结合跨视角对应预测与可解释推理，并构建双语基准测试集，提升模型透明度。

## 📝 摘要（中文）

跨视角地理定位(CVGL)旨在识别同一地理位置不同视角图像之间的对应关系。然而，现有的CVGL方法通常局限于单一视角或模态，并且其直接视觉匹配策略缺乏可解释性：它们只能确定两幅图像是否对应，而不能解释匹配背后的原因。本文提出了GLEAM-C，一个基础的CVGL模型，通过将无人机图像、街道地图、全景视图和地面照片等多种视角和模态与卫星图像对齐，从而统一了它们。我们的框架通过优化的实现提高了训练效率，并通过两阶段训练策略实现了与先前特定模态CVGL模型相当的精度。此外，为了解决传统CVGL方法缺乏可解释性的问题，我们利用多模态大型语言模型(MLLM)的推理能力，提出了一个新的任务GLEAM-X，它将跨视角对应预测与可解释的推理相结合。为了支持这项任务，我们使用GPT-4o和Doubao-1.5-Thinking-Vision-Pro构建了一个双语基准，以生成训练和测试数据。测试集通过详细的人工修订进一步完善，从而能够系统地评估可解释的跨视角推理，并提高地理定位的透明度和可扩展性。GLEAM-C和GLEAM-X共同构成了一个全面的CVGL流程，它集成了多模态、多视角对齐与可解释的对应关系分析，统一了准确的跨视角匹配与可解释的推理，并通过使模型能够更好地解释和匹配来推进地理定位。

## 🔬 方法详解

**问题定义**：现有的跨视角地理定位方法主要存在两个痛点：一是视角和模态单一，难以处理复杂场景；二是缺乏可解释性，模型只能给出匹配结果，无法解释匹配的原因，这限制了其在实际应用中的可靠性。

**核心思路**：GLEAM的核心思路是将多种视角和模态的信息统一到一个框架中，并通过引入多模态大型语言模型（MLLM）来增强模型的可解释性。具体来说，GLEAM-C负责多模态对齐和匹配，而GLEAM-X则负责利用MLLM进行推理，解释匹配的原因。

**技术框架**：GLEAM框架包含两个主要部分：GLEAM-C和GLEAM-X。GLEAM-C是一个多模态对齐和匹配模型，它将不同视角和模态的图像（如无人机图像、街景图像、全景图像等）与卫星图像对齐。GLEAM-X则利用MLLM的推理能力，对GLEAM-C的匹配结果进行解释，生成自然语言描述，说明为什么两幅图像是对应的。整个流程包括数据预处理、特征提取、跨模态对齐、匹配预测和可解释推理等步骤。

**关键创新**：GLEAM的关键创新在于将多模态对齐和可解释推理结合起来，提出了GLEAM-X任务，并构建了相应的双语基准测试集。这使得模型不仅能够进行准确的跨视角匹配，还能够解释匹配的原因，从而提高了模型的可信度和可靠性。此外，GLEAM-C通过优化的实现提高了训练效率，使其能够处理大规模的多模态数据。

**关键设计**：GLEAM-C采用了两阶段训练策略，首先进行预训练，然后在特定任务上进行微调。GLEAM-X则利用GPT-4o和Doubao-1.5-Thinking-Vision-Pro等MLLM生成训练数据，并通过人工修订提高数据质量。损失函数方面，可能采用了对比损失或三元组损失来优化跨模态对齐。具体的网络结构细节（如backbone的选择、attention机制的使用等）在论文中应该有更详细的描述。

## 📊 实验亮点

GLEAM-C在多视角地理定位任务上取得了与特定模态模型相当的精度，同时提高了训练效率。GLEAM-X通过引入可解释推理，显著提升了模型的可信度。论文构建的双语基准测试集为可解释跨视角推理的研究提供了重要的数据支持，并经过人工修订，保证了测试集的质量。

## 🎯 应用场景

GLEAM在城市规划、自动驾驶、灾害评估、环境监测等领域具有广泛的应用前景。例如，可以利用GLEAM对无人机拍摄的灾区图像与卫星图像进行匹配，快速评估灾情；也可以用于自动驾驶车辆的定位和导航，提高车辆在复杂环境下的感知能力。未来，GLEAM有望成为构建更智能、更可靠的地理信息系统的关键技术。

## 📄 摘要（原文）

> Cross-View Geo-Localization (CVGL) focuses on identifying correspondences between images captured from distinct perspectives of the same geographical location. However, existing CVGL approaches are typically restricted to a single view or modality, and their direct visual matching strategy lacks interpretability: they only determine whether two images correspond, without explaining the rationale behind the match. In this paper, we present GLEAM-C, a foundational CVGL model that unifies multiple views and modalities-including UAV imagery, street maps, panoramic views, and ground photographs-by aligning them exclusively with satellite imagery. Our framework enhances training efficiency through optimized implementation while achieving accuracy comparable to prior modality-specific CVGL models through a two-phase training strategy. Moreover, to address the lack of interpretability in traditional CVGL methods, we leverage the reasoning capabilities of multimodal large language models (MLLMs) to propose a new task, GLEAM-X, which combines cross-view correspondence prediction with explainable reasoning. To support this task, we construct a bilingual benchmark using GPT-4o and Doubao-1.5-Thinking-Vision-Pro to generate training and testing data. The test set is further refined through detailed human revision, enabling systematic evaluation of explainable cross-view reasoning and advancing transparency and scalability in geo-localization. Together, GLEAM-C and GLEAM-X form a comprehensive CVGL pipeline that integrates multi-modal, multi-view alignment with interpretable correspondence analysis, unifying accurate cross-view matching with explainable reasoning and advancing Geo-Localization by enabling models to better Explain And Match. Code and datasets used in this work will be made publicly accessible at https://github.com/Lucky-Lance/GLEAM.

