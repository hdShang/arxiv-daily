---
layout: default
title: "VoiceAssistant-Eval: Benchmarking AI Assistants across Listening, Speaking, and Viewing"
---

# VoiceAssistant-Eval: Benchmarking AI Assistants across Listening, Speaking, and Viewing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22651" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22651v1</a>
  <a href="https://arxiv.org/pdf/2509.22651.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22651v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22651v1', 'VoiceAssistant-Eval: Benchmarking AI Assistants across Listening, Speaking, and Viewing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Wang, Houxing Ren, Zimu Lu, Mingjie Zhan, Hongsheng Li

**分类**: cs.CL, cs.AI, cs.CV, cs.HC, cs.SD

**发布日期**: 2025-09-26

**🔗 代码/项目**: [PROJECT_PAGE](https://mathllm.github.io/VoiceAssistantEval/)

---

## 💡 一句话要点

**VoiceAssistant-Eval：一个综合性的AI助手评测基准，覆盖听觉、语音和视觉能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI助手评测` `多模态学习` `语音识别` `语音合成` `图像理解` `基准数据集` `人机交互`

## 📋 核心要点

1. 现有AI助手评测基准无法全面评估其听觉、语音和视觉能力，限制了相关技术发展。
2. 提出VoiceAssistant-Eval，一个包含10497个示例的综合基准，覆盖13个任务类别，评估AI助手多模态能力。
3. 实验表明，开源模型在某些方面可与专有模型竞争，但多模态理解和鲁棒性仍有待提高。

## 📝 摘要（中文）

大型语言模型和多模态系统能力的不断增强激发了人们对语音优先AI助手的兴趣，但现有的基准不足以评估这些系统的全部能力。我们推出了VoiceAssistant-Eval，这是一个综合性的基准，旨在评估AI助手在听觉、语音和视觉方面的能力。VoiceAssistant-Eval包含10497个精心策划的示例，涵盖13个任务类别。这些任务包括自然声音、音乐和口语对话的听觉理解；多轮对话、角色扮演模仿和各种场景的语音生成；以及高度异构的图像的视觉理解。为了证明其效用，我们评估了21个开源模型和GPT-4o-Audio，测量了响应内容和语音的质量以及它们的一致性。结果揭示了三个关键发现：(1)专有模型并非普遍优于开源模型；(2)大多数模型擅长语音任务，但在音频理解方面滞后；(3)精心设计的小型模型可以与更大的模型相媲美。值得注意的是，中等规模的Step-Audio-2-mini (7B)的听觉准确率是LLaMA-Omni2-32B-Bilingual的两倍多。然而，仍然存在挑战：多模态（音频加视觉）输入和角色扮演语音模仿任务对于当前模型来说很困难，并且在鲁棒性和安全对齐方面仍然存在显著差距。VoiceAssistant-Eval识别了这些差距，并建立了一个严格的框架，用于评估和指导下一代AI助手的开发。代码和数据将在https://mathllm.github.io/VoiceAssistantEval/ 上发布。

## 🔬 方法详解

**问题定义**：现有AI助手评测基准主要关注文本输入和输出，缺乏对听觉、语音和视觉能力的综合评估。这导致我们难以全面了解AI助手在真实世界场景中的表现，尤其是在需要处理多模态信息的复杂任务中。现有方法的痛点在于无法有效衡量AI助手在音频理解、语音生成以及多模态交互方面的能力。

**核心思路**：VoiceAssistant-Eval的核心思路是构建一个全面、多样化的评测数据集，覆盖AI助手在听觉、语音和视觉方面的关键能力。通过设计一系列具有挑战性的任务，例如自然声音识别、多轮对话、角色扮演模仿和图像理解，来评估AI助手在不同场景下的性能。该基准旨在揭示现有模型的优势和不足，并为未来的研究提供指导。

**技术框架**：VoiceAssistant-Eval包含三个主要模块：听觉评估、语音评估和视觉评估。听觉评估模块包含自然声音、音乐和口语对话等任务，用于评估模型对音频信息的理解能力。语音评估模块包含多轮对话、角色扮演模仿和各种场景等任务，用于评估模型的语音生成能力。视觉评估模块包含高度异构的图像，用于评估模型对图像信息的理解能力。整个框架通过统一的评估指标来衡量模型在不同任务上的表现，从而实现对AI助手能力的全面评估。

**关键创新**：VoiceAssistant-Eval最重要的技术创新点在于其综合性和多样性。与现有的基准相比，VoiceAssistant-Eval不仅覆盖了听觉、语音和视觉三种模态，还包含了各种具有挑战性的任务，例如角色扮演语音模仿和多模态输入。这种设计使得VoiceAssistant-Eval能够更全面地评估AI助手的真实世界性能，并为未来的研究提供更丰富的实验数据。与现有方法的本质区别在于，VoiceAssistant-Eval更加关注AI助手在多模态环境下的交互能力，而不仅仅是单模态的理解或生成能力。

**关键设计**：在数据集构建方面，作者精心挑选了10497个示例，并对每个示例进行了详细的标注。在评估指标方面，作者采用了多种指标来衡量模型在不同任务上的表现，包括准确率、BLEU分数和语音质量评估指标。此外，作者还设计了一套统一的评估流程，以确保评估结果的可靠性和可比性。具体的参数设置、损失函数和网络结构等技术细节取决于被评估的模型，VoiceAssistant-Eval主要提供一个统一的评估平台。

## 📊 实验亮点

实验结果表明，专有模型并非在所有任务上都优于开源模型，中等规模的Step-Audio-2-mini (7B)在听觉准确率上超过了LLaMA-Omni2-32B-Bilingual两倍以上。然而，多模态输入和角色扮演语音模仿任务对现有模型仍然具有挑战性，并且在鲁棒性和安全对齐方面存在显著差距。这些发现为未来的研究方向提供了重要的启示。

## 🎯 应用场景

VoiceAssistant-Eval可应用于评估和改进各种语音助手，例如智能音箱、车载助手和移动应用中的语音交互功能。该基准能够帮助研究人员和开发者识别现有模型的不足，并指导下一代AI助手的开发，使其在多模态交互、鲁棒性和安全性方面得到提升。这有助于推动人机交互技术的进步，并为用户提供更自然、更智能的语音助手体验。

## 📄 摘要（原文）

> The growing capabilities of large language models and multimodal systems have spurred interest in voice-first AI assistants, yet existing benchmarks are inadequate for evaluating the full range of these systems' capabilities. We introduce VoiceAssistant-Eval, a comprehensive benchmark designed to assess AI assistants across listening, speaking, and viewing. VoiceAssistant-Eval comprises 10,497 curated examples spanning 13 task categories. These tasks include natural sounds, music, and spoken dialogue for listening; multi-turn dialogue, role-play imitation, and various scenarios for speaking; and highly heterogeneous images for viewing. To demonstrate its utility, we evaluate 21 open-source models and GPT-4o-Audio, measuring the quality of the response content and speech, as well as their consistency. The results reveal three key findings: (1) proprietary models do not universally outperform open-source models; (2) most models excel at speaking tasks but lag in audio understanding; and (3) well-designed smaller models can rival much larger ones. Notably, the mid-sized Step-Audio-2-mini (7B) achieves more than double the listening accuracy of LLaMA-Omni2-32B-Bilingual. However, challenges remain: multimodal (audio plus visual) input and role-play voice imitation tasks are difficult for current models, and significant gaps persist in robustness and safety alignment. VoiceAssistant-Eval identifies these gaps and establishes a rigorous framework for evaluating and guiding the development of next-generation AI assistants. Code and data will be released at https://mathllm.github.io/VoiceAssistantEval/ .

