---
layout: default
title: "Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents"
---

# Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24878" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24878v1</a>
  <a href="https://arxiv.org/pdf/2505.24878.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24878v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24878v1', 'Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaxin Luo, Zhaoyi Li, Jiacheng Liu, Jiacheng Cui, Xiaohan Zhao, Zhiqiang Shen

**分类**: cs.AI, cs.CL, cs.CV, cs.LG

**发布日期**: 2025-05-30

**备注**: Code at: https://github.com/MetaAgentX/OpenCaptchaWorld

---

## 💡 一句话要点

**提出Open CaptchaWorld以解决多模态LLM代理在CAPTCHA挑战中的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态LLM` `CAPTCHA` `推理深度` `视觉推理` `自动化测试` `网络安全` `人机交互`

## 📋 核心要点

1. 现有的多模态LLM代理在处理CAPTCHA等交互式推理任务时表现不佳，成功率远低于人类。
2. 论文提出Open CaptchaWorld平台，通过225个多样化的CAPTCHA测试多模态LLM代理的视觉推理和交互能力。
3. 实验结果显示，当前多模态LLM代理的成功率最高仅为40.0%，远低于人类的93.3%，揭示了其在复杂推理任务中的局限性。

## 📝 摘要（中文）

CAPTCHA一直是部署网络代理的关键瓶颈，阻碍了其完成端到端自动化任务。尽管现代多模态LLM代理在静态感知任务中表现出色，但在处理交互式、多步骤推理挑战（如CAPTCHA）方面的能力尚未得到充分测试。为了解决这一问题，我们提出了Open CaptchaWorld，这是第一个专门设计用于评估多模态LLM代理视觉推理和交互能力的网络基准平台。我们的基准涵盖20种现代CAPTCHA类型，共计225个CAPTCHA，并引入了一种新的度量标准：CAPTCHA推理深度，量化了解决每个难题所需的认知和运动步骤数量。实验结果表明，人类的成功率接近完美，而最先进的多模态LLM代理的成功率最高仅为40.0%，远低于人类的93.3%。这突显了Open CaptchaWorld作为诊断当前多模态代理局限性的重要基准，并指导更强大的多模态推理系统的发展。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态LLM代理在处理CAPTCHA等复杂推理任务时的能力不足。现有方法在面对动态和交互式的挑战时，表现出显著的局限性，导致成功率远低于人类水平。

**核心思路**：论文的核心思路是构建一个专门的基准平台Open CaptchaWorld，旨在通过多样化的CAPTCHA测试，系统性地评估和提升多模态LLM代理的视觉推理和交互能力。通过引入新的度量标准CAPTCHA推理深度，量化解决问题所需的认知步骤，帮助研究者更好地理解代理的推理过程。

**技术框架**：Open CaptchaWorld平台的整体架构包括CAPTCHA生成模块、评估模块和数据分析模块。CAPTCHA生成模块负责创建多样化的CAPTCHA类型，评估模块用于测试代理的表现，数据分析模块则对结果进行统计和分析。

**关键创新**：最重要的技术创新点在于引入了CAPTCHA推理深度这一新度量标准，能够量化解决CAPTCHA所需的认知和运动步骤。这一创新使得对多模态LLM代理的评估更加全面和深入，能够揭示其在复杂推理任务中的具体弱点。

**关键设计**：在设计中，CAPTCHA的类型和难度经过精心选择，以确保覆盖多种推理场景。同时，评估过程中采用了标准化的评分机制，以确保结果的可比性和可靠性。

## 📊 实验亮点

实验结果显示，当前最先进的多模态LLM代理在CAPTCHA任务中的成功率最高仅为40.0%，而人类的成功率高达93.3%。这一显著差距突显了Open CaptchaWorld在评估和改进多模态推理系统中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化测试、网络安全和人机交互等。通过提供一个标准化的评估平台，Open CaptchaWorld能够帮助研究人员和开发者更好地理解和提升多模态LLM代理在复杂推理任务中的表现，推动相关技术的进步与应用。

## 📄 摘要（原文）

> CAPTCHAs have been a critical bottleneck for deploying web agents in real-world applications, often blocking them from completing end-to-end automation tasks. While modern multimodal LLM agents have demonstrated impressive performance in static perception tasks, their ability to handle interactive, multi-step reasoning challenges like CAPTCHAs is largely untested. To address this gap, we introduce Open CaptchaWorld, the first web-based benchmark and platform specifically designed to evaluate the visual reasoning and interaction capabilities of MLLM-powered agents through diverse and dynamic CAPTCHA puzzles. Our benchmark spans 20 modern CAPTCHA types, totaling 225 CAPTCHAs, annotated with a new metric we propose: CAPTCHA Reasoning Depth, which quantifies the number of cognitive and motor steps required to solve each puzzle. Experimental results show that humans consistently achieve near-perfect scores, state-of-the-art MLLM agents struggle significantly, with success rates at most 40.0% by Browser-Use Openai-o3, far below human-level performance, 93.3%. This highlights Open CaptchaWorld as a vital benchmark for diagnosing the limits of current multimodal agents and guiding the development of more robust multimodal reasoning systems. Code and Data are available at this https URL.

