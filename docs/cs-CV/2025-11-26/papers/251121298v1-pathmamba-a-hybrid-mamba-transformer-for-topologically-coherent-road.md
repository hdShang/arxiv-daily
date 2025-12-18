---
layout: default
title: PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery
---

# PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21298" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21298v1</a>
  <a href="https://arxiv.org/pdf/2511.21298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21298v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21298v1', 'PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jules Decaestecker, Nicolas Vigne

**分类**: cs.CV

**发布日期**: 2025-11-26

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**提出PathMamba，用于卫星图像中拓扑连续的道路分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `道路分割` `卫星图像` `Mamba` `Transformer` `拓扑连续性` `遥感图像处理` `深度学习`

## 📋 核心要点

1. 现有道路分割方法依赖Vision Transformers，计算复杂度高，难以在资源受限平台部署。
2. PathMamba结合Mamba的序列建模和Transformer的全局推理，提升道路分割的拓扑连续性。
3. 实验表明PathMamba在DeepGlobe和Massachusetts数据集上显著提升了拓扑连续性，并保持了计算效率。

## 📝 摘要（中文）

从卫星图像中进行道路分割，同时实现高精度和拓扑连续性，对于城市规划和灾害响应等应用至关重要。目前的方法通常依赖于Vision Transformers，它擅长捕获全局上下文，但其二次复杂度是高效部署的重大障碍，尤其是在资源受限的平台上。相比之下，像Mamba这样的新兴状态空间模型提供线性时间效率，并且本质上适合于建模长的、连续的结构。我们认为这些架构具有互补的优势。为此，我们引入了PathMamba，这是一种新颖的混合架构，它将Mamba的顺序建模与Transformer的全局推理相结合。我们的设计策略性地使用Mamba块来追踪道路网络的连续性，保持拓扑结构，同时集成Transformer块以利用全局上下文来细化特征。这种方法产生了拓扑结构上更优越的分割图，而没有纯粹基于注意力的模型那样令人望而却步的扩展成本。我们在DeepGlobe Road Extraction和Massachusetts Roads数据集上的实验表明，PathMamba设置了新的技术水平。值得注意的是，它显著提高了拓扑连续性，如APLS指标所衡量的那样，在保持计算竞争力的同时，建立了一个新的基准。

## 🔬 方法详解

**问题定义**：论文旨在解决卫星图像道路分割中，现有方法难以兼顾高精度和拓扑连续性的问题。Vision Transformers虽然能捕捉全局信息，但计算复杂度高，难以部署。传统方法在拓扑结构保持方面存在不足，导致分割结果不连续，影响实际应用。

**核心思路**：论文的核心思路是结合Mamba和Transformer的优势。Mamba擅长处理序列数据，能够有效建模道路的连续性，保持拓扑结构；Transformer擅长捕捉全局上下文信息，用于特征细化。通过混合使用这两种架构，PathMamba能够在保证精度的同时，提升道路分割结果的拓扑连续性。

**技术框架**：PathMamba的整体架构是一个混合模型，包含Mamba块和Transformer块。Mamba块主要负责追踪道路网络的连续性，保持拓扑结构；Transformer块则用于提取全局上下文信息，细化特征。具体流程可能是先通过Mamba块进行初步分割，然后利用Transformer块进行特征增强和修正，最后得到最终的分割结果。具体模块的排列顺序和连接方式未知。

**关键创新**：PathMamba的关键创新在于混合使用Mamba和Transformer，充分利用两者的优势。与纯Transformer模型相比，PathMamba降低了计算复杂度，更适合资源受限的平台。与传统方法相比，PathMamba通过Mamba块更好地保持了道路的拓扑连续性。

**关键设计**：论文中关于Mamba块和Transformer块的具体配置细节未知。可能涉及的关键设计包括：Mamba块和Transformer块的比例、连接方式，以及各自的参数设置。损失函数可能包含分割损失和拓扑损失，以同时优化分割精度和拓扑连续性。具体的网络结构细节未知。

## 📊 实验亮点

PathMamba在DeepGlobe Road Extraction和Massachusetts Roads数据集上取得了新的技术水平。通过APLS指标衡量，PathMamba显著提高了拓扑连续性，并在保持计算竞争力的同时，设立了新的基准。具体的性能数据和提升幅度未知，但强调了在拓扑连续性方面的显著改进。

## 🎯 应用场景

PathMamba在卫星图像道路分割领域具有广泛的应用前景，可用于城市规划、交通管理、灾害响应等。高精度和拓扑连续的道路分割结果有助于快速评估灾情、优化交通网络、辅助城市规划决策。该研究对遥感图像处理和地理信息系统具有重要意义，并可能推动相关领域的发展。

## 📄 摘要（原文）

> Achieving both high accuracy and topological continuity in road segmentation from satellite imagery is a critical goal for applications ranging from urban planning to disaster response. State-of-the-art methods often rely on Vision Transformers, which excel at capturing global context, yet their quadratic complexity is a significant barrier to efficient deployment, particularly for on-board processing in resource-constrained platforms. In contrast, emerging State Space Models like Mamba offer linear-time efficiency and are inherently suited to modeling long, continuous structures. We posit that these architectures have complementary strengths. To this end, we introduce PathMamba, a novel hybrid architecture that integrates Mamba's sequential modeling with the Transformer's global reasoning. Our design strategically uses Mamba blocks to trace the continuous nature of road networks, preserving topological structure, while integrating Transformer blocks to refine features with global context. This approach yields topologically superior segmentation maps without the prohibitive scaling costs of pure attention-based models. Our experiments on the DeepGlobe Road Extraction and Massachusetts Roads datasets demonstrate that PathMamba sets a new state-of-the-art. Notably, it significantly improves topological continuity, as measured by the APLS metric, setting a new benchmark while remaining computationally competitive.

