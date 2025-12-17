---
layout: default
title: Beyond Seeing: Evaluating Multimodal LLMs on Tool-Enabled Image Perception, Transformation, and Reasoning
---

# Beyond Seeing: Evaluating Multimodal LLMs on Tool-Enabled Image Perception, Transformation, and Reasoning

**arXiv**: [2510.12712v1](https://arxiv.org/abs/2510.12712) | [PDF](https://arxiv.org/pdf/2510.12712.pdf)

**作者**: Xingang Guo, Utkarsh Tyagi, Advait Gosai, Paula Vergara, Ernesto Gabriel Hernández Montoya, Chen Bo Calvin Zhang, Bin Hu, Yunzhong He, Bing Liu, Rakshith Sharma Srinivasa

---

## 💡 一句话要点

**提出IRIS基准以评估多模态大语言模型在工具辅助图像感知、变换与推理中的能力**

**关键词**: `多模态大语言模型` `图像交互推理` `工具集成` `基准评估` `视觉变换` `开放任务`

## 📋 核心要点

1. 核心问题：现有基准多将图像视为静态输入，未充分探索MLLMs在动态图像变换与工具集成中的能力。
2. 方法要点：引入IRIS基准，包含1,204个开放视觉任务，涵盖感知、变换和推理，支持多轮交互。
3. 实验或效果：当前MLLMs表现不佳，最强模型仅达18.68%通过率，工具使用行为存在差异。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) are increasingly applied in
> real-world scenarios where user-provided images are often imperfect, requiring
> active image manipulations such as cropping, editing, or enhancement to uncover
> salient visual cues. Beyond static visual perception, MLLMs must also think
> with images: dynamically transforming visual content and integrating it with
> other tools to solve complex tasks. However, this shift from treating vision as
> passive context to a manipulable cognitive workspace remains underexplored.
> Most existing benchmarks still follow a think about images paradigm, where
> images are regarded as static inputs. To address this gap, we introduce IRIS,
> an Interactive Reasoning with Images and Systems that evaluates MLLMs' ability
> to perceive, transform, and reason across complex visual-textual tasks under
> the think with images paradigm. IRIS comprises 1,204 challenging, open-ended
> vision tasks (603 single-turn, 601 multi-turn) spanning across five diverse
> domains, each paired with detailed rubrics to enable systematic evaluation. Our
> evaluation shows that current MLLMs struggle with tasks requiring effective
> integration of vision and general-purpose tools. Even the strongest model
> (GPT-5-think) reaches only 18.68% pass rate. We further observe divergent
> tool-use behaviors, with OpenAI models benefiting from diverse image
> manipulations while Gemini-2.5-pro shows no improvement. By introducing the
> first benchmark centered on think with images, IRIS offers critical insights
> for advancing visual intelligence in MLLMs.

