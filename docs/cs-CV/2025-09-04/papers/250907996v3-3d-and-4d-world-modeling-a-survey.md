---
layout: default
title: "3D and 4D World Modeling: A Survey"
---

# 3D and 4D World Modeling: A Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07996" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07996v3</a>
  <a href="https://arxiv.org/pdf/2509.07996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07996v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07996v3', '3D and 4D World Modeling: A Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingdong Kong, Wesley Yang, Jianbiao Mei, Youquan Liu, Ao Liang, Dekai Zhu, Dongyue Lu, Wei Yin, Xiaotao Hu, Mingkai Jia, Junyuan Deng, Kaiwen Zhang, Yang Wu, Tianyi Yan, Shenyuan Gao, Song Wang, Linfeng Li, Liang Pan, Yong Liu, Jianke Zhu, Wei Tsang Ooi, Steven C. H. Hoi, Ziwei Liu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-04 (更新: 2025-12-03)

**备注**: Survey; 50 pages, 10 figures, 14 tables; GitHub Repo at https://github.com/worldbench/awesome-3d-4d-world-models

**🔗 代码/项目**: [GITHUB](https://github.com/worldbench/awesome-3d-4d-world-models)

---

## 💡 一句话要点

**对3D和4D世界建模与生成进行全面综述，填补了该领域系统性研究的空白。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D世界建模` `4D世界建模` `世界模型` `场景理解` `人工智能`

## 📋 核心要点

1. 现有世界建模研究主要集中在2D图像和视频，忽略了3D/4D数据（如RGB-D、LiDAR）的潜力。
2. 论文对3D/4D世界建模进行了全面综述，建立了统一的定义和分类体系，填补了领域空白。
3. 论文总结了3D/4D世界建模的数据集、评估指标、应用场景和未来方向，为后续研究提供参考。

## 📝 摘要（中文）

世界建模已成为人工智能研究的基石，使智能体能够理解、表示和预测其所处的动态环境。虽然先前的工作主要强调用于2D图像和视频数据的生成方法，但它们忽略了快速增长的、利用原生3D和4D表示（如RGB-D图像、 occupancy grids 和 LiDAR 点云）进行大规模场景建模的研究。同时，由于缺乏对“世界模型”的标准化定义和分类，导致文献中出现零散且有时不一致的说法。本综述通过首次专门针对3D和4D世界建模和生成的全面回顾来解决这些差距。我们建立了精确的定义，引入了一个结构化的分类，涵盖了基于视频（VideoGen）、基于 occupancy（OccGen）和基于 LiDAR（LiDARGen）的方法，并系统地总结了针对3D/4D设置量身定制的数据集和评估指标。我们进一步讨论了实际应用，确定了开放的挑战，并强调了有希望的研究方向，旨在为推进该领域提供一个连贯和基础的参考。

## 🔬 方法详解

**问题定义**：现有世界建模研究主要集中于2D图像和视频，缺乏对原生3D和4D数据（如RGB-D图像、occupancy grids和LiDAR点云）的充分利用。此外，领域内缺乏对“世界模型”的统一标准定义和分类，导致研究方向分散，结论不一致。

**核心思路**：本论文旨在通过对3D和4D世界建模与生成方法进行全面综述，填补领域内的空白。核心思路是建立精确的定义，构建结构化的分类体系，并系统地总结相关数据集、评估指标、应用场景和未来研究方向，从而为该领域提供一个连贯和基础的参考。

**技术框架**：论文构建了一个三分支的分类框架，分别对应于基于视频（VideoGen）、基于 occupancy（OccGen）和基于 LiDAR（LiDARGen）的方法。对于每个分支，论文都详细讨论了其代表性方法，并分析了它们的优缺点。此外，论文还总结了常用的数据集和评估指标，并探讨了实际应用和未来研究方向。

**关键创新**：本论文的关键创新在于它是第一个专门针对3D和4D世界建模和生成的全面综述。它通过建立精确的定义和结构化的分类体系，为该领域的研究提供了一个统一的框架。此外，论文还系统地总结了相关数据集、评估指标、应用场景和未来研究方向，为后续研究提供了重要的参考。

**关键设计**：论文的关键设计在于其三分支的分类框架（VideoGen, OccGen, LiDARGen）。这种分类方式能够清晰地反映不同类型3D/4D数据的特点，并方便研究者根据自己的研究方向选择合适的方法。此外，论文还对每个分支的代表性方法进行了详细的分析，并总结了常用的数据集和评估指标，为研究者提供了全面的信息。

## 📊 实验亮点

该综述论文系统性地整理了3D/4D世界建模领域的研究进展，并构建了统一的分类框架。论文总结了各类数据集和评估指标，为后续研究提供了便捷的参考。开源项目（https://github.com/worldbench/awesome-3d-4d-world-models）进一步方便了研究者快速了解该领域。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、虚拟现实/增强现实、城市规划等领域。通过对3D/4D环境的建模和预测，可以提高智能体在复杂环境中的感知和决策能力，从而实现更安全、更高效的智能化应用。

## 📄 摘要（原文）

> World modeling has become a cornerstone in AI research, enabling agents to understand, represent, and predict the dynamic environments they inhabit. While prior work largely emphasizes generative methods for 2D image and video data, they overlook the rapidly growing body of work that leverages native 3D and 4D representations such as RGB-D imagery, occupancy grids, and LiDAR point clouds for large-scale scene modeling. At the same time, the absence of a standardized definition and taxonomy for ``world models'' has led to fragmented and sometimes inconsistent claims in the literature. This survey addresses these gaps by presenting the first comprehensive review explicitly dedicated to 3D and 4D world modeling and generation. We establish precise definitions, introduce a structured taxonomy spanning video-based (VideoGen), occupancy-based (OccGen), and LiDAR-based (LiDARGen) approaches, and systematically summarize datasets and evaluation metrics tailored to 3D/4D settings. We further discuss practical applications, identify open challenges, and highlight promising research directions, aiming to provide a coherent and foundational reference for advancing the field. A systematic summary of existing literature is available at https://github.com/worldbench/awesome-3d-4d-world-models

