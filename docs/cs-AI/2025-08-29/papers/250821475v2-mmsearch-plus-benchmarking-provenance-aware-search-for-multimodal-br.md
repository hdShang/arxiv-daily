---
layout: default
title: "MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents"
---

# MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21475" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21475v2</a>
  <a href="https://arxiv.org/pdf/2508.21475.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21475v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21475v2', 'MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xijia Tao, Yihua Teng, Xinxing Su, Xinyu Fu, Jihao Wu, Chaofan Tao, Ziru Liu, Haoli Bai, Rui Liu, Lingpeng Kong

**分类**: cs.AI

**发布日期**: 2025-08-29 (更新: 2025-09-26)

**备注**: Project Page: https://mmsearch-plus.github.io

---

## 💡 一句话要点

**提出MMSearch-Plus以解决多模态搜索中的推理不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态搜索` `推理能力` `视觉信息` `模型框架` `标记集模块`

## 📋 核心要点

1. 现有多模态浏览基准缺乏真正的多模态推理能力，许多任务可用文本启发式解决，未能充分利用视觉信息。
2. 论文提出MMSearch-Plus基准，通过要求细粒度视觉线索的提取与传播，强化多模态理解，提升检索的准确性。
3. 在评估中，最强系统的端到端准确率达到36.0%，集成SoM模块在多个设置中均有显著提升，最高提高3.9个百分点。

## 📝 摘要（中文）

现有的多模态浏览基准往往未能真正要求多模态推理，因为许多任务可以仅通过文本启发式解决，而无需视觉验证。我们引入MMSearch-Plus，这是一个包含311个任务的基准，强制要求通过迭代的图像-文本检索和交叉验证在检索噪声下提取和传播细粒度的视觉线索。我们的策划程序提出的问题要求从空间线索和时间轨迹推断出图像外的事实，如事件、日期和场所。除了数据集，我们还提供了一个与模型无关的代理框架，配备标准浏览工具和一个标记集模块（SoM），使代理能够放置标记、裁剪子区域并发起针对性的图像/文本搜索。SoM实现了基于来源的缩放和检索，并提高了多步骤推理的鲁棒性。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有多模态搜索基准未能有效利用视觉信息，导致推理能力不足，无法应对真实世界的复杂检索任务。

**核心思路**：论文的核心思路是通过MMSearch-Plus基准，要求在检索过程中提取和传播细粒度的视觉线索，从而增强多模态理解能力。设计上强调了图像与文本的交互作用，确保推理过程的全面性。

**技术框架**：整体架构包括数据集构建、模型框架和SoM模块。数据集包含311个任务，模型框架支持多种MLLM，SoM模块用于标记、裁剪和检索，形成闭环反馈机制。

**关键创新**：最重要的技术创新在于引入了SoM模块，使得代理能够进行基于来源的缩放和检索，显著提高了多步骤推理的鲁棒性。这一设计与传统方法相比，增强了对视觉信息的利用。

**关键设计**：关键设计包括SoM模块的实现，支持标记和裁剪功能，损失函数的选择确保了模型在多模态任务中的有效性，网络结构则采用了适应性强的架构以支持不同类型的输入。

## 📊 实验亮点

实验结果显示，最强系统在MMSearch-Plus基准上的端到端准确率达到36.0%，集成SoM模块后在多个设置中均有显著提升，最高提高3.9个百分点。这表明SoM模块在多步骤推理中的有效性和重要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能搜索引擎、虚拟助手和多模态信息检索系统。通过提升多模态理解能力，MMSearch-Plus可为用户提供更准确的搜索结果，改善人机交互体验，未来可能推动相关技术在教育、医疗和娱乐等领域的广泛应用。

## 📄 摘要（原文）

> Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by requiring extraction and propagation of fine-grained visual cues through iterative image-text retrieval and cross-validation under retrieval noise. Our curation procedure seeds questions whose answers require extrapolating from spatial cues and temporal traces to out-of-image facts such as events, dates, and venues. Beyond the dataset, we provide a model-agnostic agent framework with standard browsing tools and a set-of-mark (SoM) module, which lets the agent place marks, crop subregions, and launch targeted image/text searches. SoM enables provenance-aware zoom-and-retrieve and improves robustness in multi-step reasoning. We evaluated closed- and open-source MLLMs in this framework. The strongest system achieves an end-to-end accuracy of 36.0%, and integrating SoM produces consistent gains in multiple settings, with improvements up to +3.9 points. From failure analysis, we observe recurring errors in locating relevant webpages and distinguishing between visually similar events. These results underscore the challenges of real-world multimodal search and establish MMSearch-Plus as a rigorous benchmark for advancing agentic MLLMs.

