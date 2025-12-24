---
layout: default
title: "Thinking with Sound: Audio Chain-of-Thought Enables Multimodal Reasoning in Large Audio-Language Models"
---

# Thinking with Sound: Audio Chain-of-Thought Enables Multimodal Reasoning in Large Audio-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21749" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21749v1</a>
  <a href="https://arxiv.org/pdf/2509.21749.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21749v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21749v1', 'Thinking with Sound: Audio Chain-of-Thought Enables Multimodal Reasoning in Large Audio-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Xiong, Yujun Cai, Zhecheng Li, Junsong Yuan, Yiwei Wang

**分类**: cs.CL, cs.SD

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出Thinking-with-Sound框架，增强LALM在复杂声学场景下的多模态推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频语言模型` `多模态推理` `链式思考` `鲁棒性` `声学分析`

## 📋 核心要点

1. 现有LALM在复杂声学场景下的推理能力不足，缺乏对音频信号的有效分析和处理工具。
2. TwS框架通过结合语言推理和实时音频域分析，使LALM能够主动“思考”音频，进行多模态推理。
3. 在MELD-Hard1k基准测试中，TwS显著提高了LALM的鲁棒性，准确率提升高达36.61%。

## 📝 摘要（中文）

现有的大型音频-语言模型(LALM)在语音翻译和音频问答等任务上表现出色，但在复杂声学场景中的音频推理任务中存在显著局限。这些场景通常需要噪声抑制、声源分离和精确的时间对齐等声学工具，而目前的LALM缺乏这些能力。为了解决这个问题，我们提出了Thinking-with-Sound (TwS)框架，通过结合语言推理和实时音频域分析，为LALM配备了Audio CoT。与将音频视为静态输入的方法不同，TwS使模型能够主动地“思考”音频信号，通过多模态推理执行数值分析和数字操作。为了评估该方法，我们构建了MELD-Hard1k，这是一个通过引入各种声学扰动而创建的新的鲁棒性基准。实验表明，最先进的LALM在MELD-Hard1k上性能显著下降，与干净音频相比，准确率下降超过50%。TwS在鲁棒性方面取得了显著的改进，证明了其有效性和可扩展性：小型模型的绝对准确率提高了24.73%，而大型模型的改进幅度一致地扩展到36.61%。我们的研究结果表明，Audio CoT可以显著提高鲁棒性而无需重新训练，为开发更强大的音频理解系统开辟了新的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决大型音频-语言模型(LALM)在复杂声学场景下进行音频推理时表现不佳的问题。现有方法通常将音频视为静态输入，缺乏利用声学工具（如噪声抑制、声源分离等）进行动态分析和处理的能力，导致在存在噪声、混响等干扰时性能显著下降。

**核心思路**：论文的核心思路是引入“Thinking-with-Sound (TwS)”框架，赋予LALM在推理过程中主动分析和处理音频信号的能力。TwS通过结合语言推理和实时音频域分析，使模型能够像人类一样，利用声学工具对音频进行预处理和分析，从而提高在复杂声学环境下的鲁棒性。

**技术框架**：TwS框架的核心是Audio Chain-of-Thought (Audio CoT)。整体流程如下：1) 接收音频和文本输入；2) LALM根据文本提示生成推理步骤，这些步骤可能包括调用声学工具进行音频分析或处理；3) 根据推理步骤，调用相应的声学工具对音频进行处理，并将处理结果反馈给LALM；4) LALM结合处理后的音频信息和文本信息，进行下一步推理，直至得到最终答案。

**关键创新**：最重要的技术创新点在于将音频处理工具集成到LALM的推理过程中，使模型能够动态地利用这些工具来改善音频质量和提取相关信息。与现有方法将音频视为静态输入不同，TwS允许模型主动地“思考”音频，并根据需要调用不同的声学工具。

**关键设计**：TwS框架的关键设计包括：1) 如何选择和集成合适的声学工具；2) 如何设计有效的文本提示，引导LALM调用这些工具；3) 如何将声学工具的处理结果有效地融入到LALM的推理过程中。论文中可能涉及具体的参数设置、损失函数或网络结构，但摘要中未明确提及，具体细节未知。

## 📊 实验亮点

实验结果表明，TwS框架在MELD-Hard1k基准测试中显著提高了LALM的鲁棒性。小型模型的绝对准确率提高了24.73%，而大型模型的提升幅度高达36.61%。这些结果表明，TwS框架能够有效地增强LALM在复杂声学环境下的推理能力，且无需重新训练模型。

## 🎯 应用场景

该研究成果可应用于语音助手、智能家居、自动驾驶等领域，提升设备在复杂声学环境下的语音识别和理解能力。例如，在嘈杂的街道上，自动驾驶系统可以利用TwS框架对语音指令进行降噪处理，从而更准确地理解驾驶员的意图，提高驾驶安全性。未来，该技术有望推动人机交互更加自然和智能。

## 📄 摘要（原文）

> Recent Large Audio-Language Models (LALMs) have shown strong performance on various audio understanding tasks such as speech translation and Audio Q\&A. However, they exhibit significant limitations on challenging audio reasoning tasks in complex acoustic scenarios. These situations would greatly benefit from the use of acoustic tools like noise suppression, source separation, and precise temporal alignment, but current LALMs lack access to such tools. To address this limitation, we introduce Thinking-with-Sound (TwS), a framework that equips LALMs with Audio CoT by combining linguistic reasoning with on-the-fly audio-domain analysis. Unlike existing approaches that treat audio as static input, TwS enables models to actively think with audio signals, performing numerical analysis and digital manipulation through multimodal reasoning. To evaluate this approach, we construct MELD-Hard1k, a new robustness benchmark created by introducing various acoustic perturbations. Experiments reveal that state-of-the-art LALMs suffer dramatic performance degradation on MELD-Hard1k, with accuracy dropping by more than $50\%$ compared to clean audio. TwS achieves substantial improvements in robustness, demonstrating both effectiveness and scalability: small models gain $24.73\%$ absolute accuracy, with improvements scaling consistently up to $36.61\%$ for larger models. Our findings demonstrate that Audio CoT can significantly enhance robustness without retraining, opening new directions for developing more robust audio understanding systems.

