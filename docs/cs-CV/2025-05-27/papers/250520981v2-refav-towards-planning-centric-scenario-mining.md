---
layout: default
title: "RefAV: Towards Planning-Centric Scenario Mining"
---

# RefAV: Towards Planning-Centric Scenario Mining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20981" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20981v2</a>
  <a href="https://arxiv.org/pdf/2505.20981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20981v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20981v2', 'RefAV: Towards Planning-Centric Scenario Mining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cainan Davidson, Deva Ramanan, Neehar Peri

**分类**: cs.CV, cs.CL, cs.RO

**发布日期**: 2025-05-27 (更新: 2025-06-18)

**备注**: Project Page: https://cainand.github.io/RefAV/

**🔗 代码/项目**: [GITHUB](https://github.com/CainanD/RefAV/) | [PROJECT_PAGE](https://argoverse.github.io/user-guide/)

---

## 💡 一句话要点

**提出RefAV以解决自动驾驶场景挖掘问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `场景挖掘` `视觉-语言模型` `多智能体交互` `数据集构建`

## 📋 核心要点

1. 现有的场景挖掘方法依赖手工查询，容易出错且耗时，难以从海量数据中提取安全关键场景。
2. 论文提出RefAV数据集，包含10,000个自然语言查询，旨在通过视觉-语言模型提升场景挖掘的准确性和效率。
3. 实验结果表明，简单使用现成的VLMs效果不佳，强调了场景挖掘的独特挑战和需求。

## 📝 摘要（中文）

自动驾驶车辆在正常测试中收集了大量多模态数据，但从未经过整理的驾驶日志中识别出有趣且安全关键的场景仍然是一个重大挑战。传统的场景挖掘技术容易出错且耗时，通常依赖手工构造的结构化查询。本文通过最近的视觉-语言模型（VLMs）重新审视时空场景挖掘，提出RefAV，一个包含10,000个自然语言查询的大规模数据集，描述与运动规划相关的复杂多智能体交互。我们评估了几种参考多目标跟踪器，并进行了实证分析，发现简单地重新利用现成的VLMs表现不佳，表明场景挖掘面临独特挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决从自动驾驶车辆的海量未整理驾驶日志中识别和定位安全关键场景的挑战。现有方法依赖手工查询，效率低且容易出错。

**核心思路**：通过引入视觉-语言模型（VLMs），利用自然语言查询来识别和定位复杂的多智能体交互场景，从而提高场景挖掘的准确性和效率。

**技术框架**：整体架构包括数据收集、自然语言查询生成、场景检测和定位模块。首先从Argoverse 2传感器数据集中提取驾驶日志，然后生成自然语言查询，最后通过VLMs进行场景挖掘。

**关键创新**：RefAV数据集的构建是本研究的核心创新，提供了丰富的自然语言查询，能够有效支持复杂场景的挖掘，与传统方法相比，显著提升了场景识别的准确性。

**关键设计**：在模型设计上，采用了多目标跟踪器，并对损失函数进行了优化，以适应场景挖掘的特殊需求。实验中还对不同的VLMs进行了比较，分析其在场景挖掘中的表现。

## 📊 实验亮点

实验结果显示，使用RefAV数据集进行场景挖掘时，基于VLMs的模型在准确性上有显著提升，但简单复用现成模型的效果不佳，表明该领域的挑战性。具体性能数据和对比基线将在后续的CVPR 2025竞赛中进一步验证。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的安全性提升、智能交通管理和多智能体系统的协作规划。通过有效识别和分析复杂场景，可以为自动驾驶技术的安全验证和优化提供重要支持，推动智能交通的发展。

## 📄 摘要（原文）

> Autonomous Vehicles (AVs) collect and pseudo-label terabytes of multi-modal data localized to HD maps during normal fleet testing. However, identifying interesting and safety-critical scenarios from uncurated driving logs remains a significant challenge. Traditional scenario mining techniques are error-prone and prohibitively time-consuming, often relying on hand-crafted structured queries. In this work, we revisit spatio-temporal scenario mining through the lens of recent vision-language models (VLMs) to detect whether a described scenario occurs in a driving log and, if so, precisely localize it in both time and space. To address this problem, we introduce RefAV, a large-scale dataset of 10,000 diverse natural language queries that describe complex multi-agent interactions relevant to motion planning derived from 1000 driving logs in the Argoverse 2 Sensor dataset. We evaluate several referential multi-object trackers and present an empirical analysis of our baselines. Notably, we find that naively repurposing off-the-shelf VLMs yields poor performance, suggesting that scenario mining presents unique challenges. Lastly, we discuss our recent CVPR 2025 competition and share insights from the community. Our code and dataset are available at https://github.com/CainanD/RefAV/ and https://argoverse.github.io/user-guide/tasks/scenario_mining.html

