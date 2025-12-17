---
layout: default
title: LongInsightBench: A Comprehensive Benchmark for Evaluating Omni-Modal Models on Human-Centric Long-Video Understanding
---

# LongInsightBench: A Comprehensive Benchmark for Evaluating Omni-Modal Models on Human-Centric Long-Video Understanding

**arXiv**: [2510.17305v1](https://arxiv.org/abs/2510.17305) | [PDF](https://arxiv.org/pdf/2510.17305.pdf)

**作者**: ZhaoYang Han, Qihan Lin, Hao Liang, Bowen Chen, Zhou Liu, Wentao Zhang

---

## 💡 一句话要点

**提出LongInsightBench基准以评估全模态模型在人类中心长视频理解中的表现**

**关键词**: `长视频理解` `全模态模型` `基准评估` `多模态融合` `时间定位` `因果推理`

## 📋 核心要点

1. 核心问题：全模态模型在长视频理解中面临时间定位和长程因果推理挑战
2. 方法要点：构建包含视觉、音频和文本的多模态长视频基准，涵盖六种任务场景
3. 实验或效果：实验显示模型在T-Loc和CE-Caus任务中表现不佳，揭示多模态融合偏差

## 📄 摘要（原文）

> We introduce \textbf{LongInsightBench}, the first benchmark designed to
> assess models' ability to understand long videos, with a focus on human
> language, viewpoints, actions, and other contextual elements, while integrating
> \textbf{visual, audio, and text} modalities. Our benchmark excels in three key
> areas: \textbf{a) Long-Duration, Information-Dense Videos:} We carefully select
> approximately 1,000 videos from open-source datasets FineVideo based on
> duration limit and the information density of both visual and audio modalities,
> focusing on content like lectures, interviews, and vlogs, which contain rich
> language elements. \textbf{b) Diverse and Challenging Task Scenarios:} We have
> designed six challenging task scenarios, including both Intra-Event and
> Inter-Event Tasks. \textbf{c) Rigorous and Comprehensive Quality Assurance
> Pipelines:} We have developed a three-step, semi-automated data quality
> assurance pipeline to ensure the difficulty and validity of the synthesized
> questions and answer options. Based on LongInsightBench, we designed a series
> of experiments. Experimental results shows that Omni-modal models(OLMs) still
> face challenge in tasks requiring precise temporal localization (T-Loc) and
> long-range causal inference (CE-Caus). Extended experiments reveal the
> information loss and processing bias in multi-modal fusion of OLMs. Our dataset
> and code is available at
> https://anonymous.4open.science/r/LongInsightBench-910F/.

