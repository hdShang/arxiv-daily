---
layout: default
title: "Sanitize Your Responses: Mitigating Privacy Leakage in Large Language Models"
---

# Sanitize Your Responses: Mitigating Privacy Leakage in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24488" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24488v1</a>
  <a href="https://arxiv.org/pdf/2509.24488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24488v1', 'Sanitize Your Responses: Mitigating Privacy Leakage in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Fu, Huandong Wang, Junyao Gao, Guoan Wan, Tao Jiang

**分类**: cs.CL, cs.CR, cs.LG

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/wjfu99/LLM_Self_Sanitize)

---

## 💡 一句话要点

**提出Self-Sanitize框架，缓解大语言模型中的隐私泄露问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `隐私泄露` `内容安全` `实时监控` `自我修复`

## 📋 核心要点

1. 现有大语言模型缓解有害内容生成的方法主要依赖事后过滤，导致高延迟和计算开销，不适用于流式生成。
2. Self-Sanitize框架模拟人类的自我监控和修复行为，通过轻量级模块在token级别实时检测和修正有害内容。
3. 实验表明，Self-Sanitize在隐私泄露场景下，以极小开销显著提升缓解性能，同时保持模型效用。

## 📝 摘要（中文）

随着大语言模型（LLMs）在聊天机器人和代码助手等广泛应用中取得显著成功，生成有害内容的问题日益受到关注。尽管在使LLMs符合安全和伦理标准方面取得了重大进展，但对抗性提示仍然可以诱导出不良响应。现有的缓解策略主要基于事后过滤，这会引入大量的延迟或计算开销，并且与token级别的流式生成不兼容。本文介绍Self-Sanitize，这是一个受认知心理学启发的新型LLM驱动的缓解框架，它模拟了人类在对话中的自我监控和自我修复行为。Self-Sanitize包含一个轻量级的Self-Monitor模块，该模块通过表征工程在token级别持续检查LLM中的高级意图，以及一个Self-Repair模块，该模块执行有害内容的就地校正，而无需启动单独的审查对话。这种设计允许实时流式监控和无缝修复，对延迟和资源利用率的影响可忽略不计。鉴于以往的研究通常对侵犯隐私的内容关注不足，我们对四个LLM在三个隐私泄露场景中进行了广泛的实验。结果表明，Self-Sanitize以最小的开销和不降低LLM效用的情况下实现了卓越的缓解性能，为更安全的LLM部署提供了实用而强大的解决方案。我们的代码可在以下链接获得：https://github.com/wjfu99/LLM_Self_Sanitize

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLMs）在生成内容时可能存在的隐私泄露问题。现有的缓解方法，如事后过滤，会引入显著的延迟和计算开销，无法满足实时流式生成的需求。此外，以往研究对隐私泄露的关注度不足，缺乏有效的针对性解决方案。

**核心思路**：论文的核心思路是模拟人类的自我监控和自我修复机制，构建一个能够实时检测和修正有害内容的框架。通过在LLM内部署轻量级的监控和修复模块，实现对生成过程的动态干预，从而避免了传统方法的事后处理带来的延迟问题。

**技术框架**：Self-Sanitize框架主要包含两个模块：Self-Monitor和Self-Repair。Self-Monitor模块通过表征工程技术，在token级别持续监控LLM的内部状态，检测是否存在潜在的有害意图。Self-Repair模块则在检测到有害内容后，立即进行就地校正，无需启动额外的审查对话。整个过程以流式方式进行，对LLM的生成过程几乎没有延迟影响。

**关键创新**：Self-Sanitize的关键创新在于其模仿人类认知过程的实时监控和修复机制。与传统的事后过滤方法不同，Self-Sanitize能够在生成过程中动态地干预和修正有害内容，从而避免了延迟问题，并提高了缓解效率。此外，该框架的设计轻量级，对LLM的性能影响极小。

**关键设计**：Self-Monitor模块的关键设计在于如何有效地提取和分析LLM的内部表征，以准确判断是否存在有害意图。这可能涉及到对特定层的激活值进行分析，或者使用预训练的分类器来识别有害模式。Self-Repair模块的关键设计在于如何在不影响生成质量的前提下，对有害内容进行有效的修正。这可能涉及到使用特定的编辑策略，或者利用LLM自身的生成能力来生成更安全的内容。具体的参数设置、损失函数和网络结构等技术细节在论文中可能没有详细描述，属于未知信息。

## 📊 实验亮点

论文在四个LLM和三个隐私泄露场景下进行了实验，结果表明Self-Sanitize框架能够以极小的开销实现卓越的缓解性能，且不会显著降低LLM的效用。具体的性能数据和对比基线在论文中有所展示，但具体提升幅度未知。实验结果验证了Self-Sanitize框架的有效性和实用性。

## 🎯 应用场景

Self-Sanitize框架可广泛应用于各种需要安全内容生成的大语言模型应用场景，如聊天机器人、代码助手、内容创作平台等。通过实时监控和修复有害内容，该框架能够有效降低隐私泄露风险，提升用户体验，并为LLM的商业化部署提供更可靠的安全保障。未来，该技术有望进一步发展，应用于更复杂的安全场景，例如对抗性攻击防御和虚假信息检测。

## 📄 摘要（原文）

> As Large Language Models (LLMs) achieve remarkable success across a wide range of applications, such as chatbots and code copilots, concerns surrounding the generation of harmful content have come increasingly into focus. Despite significant advances in aligning LLMs with safety and ethical standards, adversarial prompts can still be crafted to elicit undesirable responses. Existing mitigation strategies are predominantly based on post-hoc filtering, which introduces substantial latency or computational overhead, and is incompatible with token-level streaming generation. In this work, we introduce Self-Sanitize, a novel LLM-driven mitigation framework inspired by cognitive psychology, which emulates human self-monitor and self-repair behaviors during conversations. Self-Sanitize comprises a lightweight Self-Monitor module that continuously inspects high-level intentions within the LLM at the token level via representation engineering, and a Self-Repair module that performs in-place correction of harmful content without initiating separate review dialogues. This design allows for real-time streaming monitoring and seamless repair, with negligible impact on latency and resource utilization. Given that privacy-invasive content has often been insufficiently focused in previous studies, we perform extensive experiments on four LLMs across three privacy leakage scenarios. The results demonstrate that Self-Sanitize achieves superior mitigation performance with minimal overhead and without degrading the utility of LLMs, offering a practical and robust solution for safer LLM deployments. Our code is available at the following link: https://github.com/wjfu99/LLM_Self_Sanitize

