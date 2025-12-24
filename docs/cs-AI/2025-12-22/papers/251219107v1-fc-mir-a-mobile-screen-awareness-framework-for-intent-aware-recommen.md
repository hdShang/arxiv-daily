---
layout: default
title: "FC-MIR: A Mobile Screen Awareness Framework for Intent-Aware Recommendation based on Frame-Compressed Multimodal Trajectory Reasoning"
---

# FC-MIR: A Mobile Screen Awareness Framework for Intent-Aware Recommendation based on Frame-Compressed Multimodal Trajectory Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19107" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19107v1</a>
  <a href="https://arxiv.org/pdf/2512.19107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19107v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19107v1', 'FC-MIR: A Mobile Screen Awareness Framework for Intent-Aware Recommendation based on Frame-Compressed Multimodal Trajectory Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Yang, Xiaoshuang Sheng, Zhengnan Zhang, Jidong Wu, Zexing Wang, Xin He, Shenghua Xu, Guanjing Xiong

**分类**: cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出FC-MIR框架，通过帧压缩多模态轨迹推理实现意图感知的移动屏幕推荐。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动UI理解` `意图识别` `多模态大语言模型` `关键帧采样` `帧压缩` `UI自动化` `人机交互`

## 📋 核心要点

1. 现有方法在移动设备上部署多模态大语言模型（MLLM）时，面临计算成本高昂和冗余帧处理效率低下的挑战。
2. FC-MIR框架通过关键帧采样和自适应连接，有效降低视觉冗余，提升MLLM在移动设备上的推理效率，同时进行意图预测。
3. 实验结果表明，该框架在保持性能的同时实现了较高的压缩率，并验证了MLLM在意图总结方面的能力，为轻量级部署奠定基础。

## 📝 摘要（中文）

本文提出FC-MIR框架，旨在解决移动UI操作轨迹中用户意图识别的问题，从而促进UI理解和任务自动化。该框架利用关键帧采样和自适应连接，减少视觉冗余，提高推理效率。同时，集成先进的闭源多模态大语言模型（MLLM）或微调模型（如Qwen3-VL），用于轨迹总结和意图预测。研究进一步扩展到预测后操作和搜索建议生成，并引入细粒度指标评估总结、预测和建议的实用性。通过UI-Agents和真实用户交互构建的UI轨迹数据集进行评估，结果表明压缩方法在50%-60%压缩率下保持性能；闭源和微调MLLM均表现出强大的意图总结能力，支持轻量级设备部署。然而，MLLM在生成有用和“令人惊讶”的建议方面仍有改进空间。最后，该框架已部署在实际环境中，集成了UI感知和UI-Agent代理，为该领域的未来发展奠定基础。

## 🔬 方法详解

**问题定义**：论文旨在解决从移动UI操作轨迹中识别用户意图的问题。现有方法，特别是直接应用MLLM的方法，在移动设备上部署时面临计算量大、效率低下的问题，主要是因为视频帧存在大量冗余信息，导致不必要的计算开销。

**核心思路**：论文的核心思路是通过减少视觉冗余来提高推理效率，同时保持意图识别的准确性。具体而言，采用关键帧采样和自适应连接的方法，从UI操作轨迹中提取最具代表性的帧，并将其输入到MLLM中进行处理。这样可以在显著减少计算量的同时，保留足够的信息用于意图理解。

**技术框架**：FC-MIR框架主要包含以下几个阶段：1) **UI轨迹数据采集**：收集UI-Agent和真实用户的UI操作轨迹数据。2) **关键帧采样**：使用算法从UI轨迹中选择关键帧，减少视觉冗余。3) **自适应连接**：将关键帧进行连接，形成MLLM的输入。4) **MLLM推理**：使用闭源MLLM或微调的开源MLLM（如Qwen3-VL）进行轨迹总结、意图预测、后操作生成和搜索建议生成。5) **评估**：使用细粒度指标评估总结、预测和建议的实用性。

**关键创新**：该论文的关键创新在于提出了帧压缩方法，通过关键帧采样和自适应连接，显著降低了MLLM处理移动UI操作轨迹时的计算量，使其更适合在移动设备上部署。此外，还提出了细粒度的评估指标，用于评估轨迹总结、意图预测和建议的实用性。

**关键设计**：关键帧采样算法的具体实现细节未知，但其目标是选择最具代表性的帧，以最大程度地保留信息并减少冗余。自适应连接方法的具体实现细节也未知，但其目标是有效地将关键帧连接起来，以便MLLM能够理解UI操作的上下文。论文中使用了闭源MLLM和微调的Qwen3-VL模型，具体微调策略未知。评估指标的设计考虑了总结、预测和建议的实用性和“令人惊讶”程度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19107v1/lc_e.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19107v1/l.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19107v1/guanjian.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FC-MIR框架在50%-60%的压缩率下仍能保持意图识别的性能。闭源和微调的MLLM在轨迹总结方面表现出色，验证了其在轻量级设备上部署的潜力。然而，MLLM在生成有用和“令人惊讶”的建议方面仍有提升空间，表明未来研究方向。

## 🎯 应用场景

该研究成果可应用于智能助手、自动化测试、用户行为分析等领域。例如，可以利用该框架构建更智能的UI自动化测试工具，或者为用户提供更个性化的应用推荐和操作建议。通过理解用户在移动设备上的操作意图，可以实现更高效、更便捷的人机交互。

## 📄 摘要（原文）

> Identifying user intent from mobile UI operation trajectories is critical for advancing UI understanding and enabling task automation agents. While Multimodal Large Language Models (MLLMs) excel at video understanding tasks, their real-time mobile deployment is constrained by heavy computational costs and inefficient redundant frame processing. To address these issues, we propose the FC-MIR framework: leveraging keyframe sampling and adaptive concatenation, it cuts visual redundancy to boost inference efficiency, while integrating state-of-the-art closed-source MLLMs or fine-tuned models (e.g., Qwen3-VL) for trajectory summarization and intent prediction. We further expand task scope to explore generating post-prediction operations and search suggestions, and introduce a fine-grained metric to evaluate the practical utility of summaries, predictions, and suggestions. For rigorous assessment, we construct a UI trajectory dataset covering scenarios from UI-Agents (Agent-I) and real user interactions (Person-I). Experimental results show our compression method retains performance at 50%-60% compression rates; both closed-source and fine-tuned MLLMs demonstrate strong intent summarization, supporting potential lightweight on-device deployment. However, MLLMs still struggle with useful and "surprising" suggestions, leaving room for improvement. Finally, we deploy the framework in a real-world setting, integrating UI perception and UI-Agent proxies to lay a foundation for future progress in this field.

