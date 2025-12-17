---
layout: default
title: QG-CoC: Question-Guided Chain-of-Captions for Large Multimodal Models
---

# QG-CoC: Question-Guided Chain-of-Captions for Large Multimodal Models

**arXiv**: [2511.03206v1](https://arxiv.org/abs/2511.03206) | [PDF](https://arxiv.org/pdf/2511.03206.pdf)

**作者**: Kuei-Chun Kao, Hsu Tzu-Yin, Yunqi Hong, Ruochen Wang, Cho-Jui Hsieh

---

## 💡 一句话要点

**提出QG-CoC零样本提示方法以解决多模态大模型在多图像推理中的感知与整合问题**

**关键词**: `多模态大语言模型` `多图像推理` `零样本提示` `链式描述` `视觉感知` `基准评估`

## 📋 核心要点

1. 多模态大模型在多图像场景中缺乏细粒度感知和有效推理能力
2. QG-CoC通过问题引导的链式描述实现任意数量图像的处理
3. 实验显示QG-CoC在多种基准测试中表现优异，尤其在挑战性场景下改进显著

## 📄 摘要（原文）

> Recently, Multimodal Large Language Models (MLLMs) encounter two key issues
> in multi-image contexts: (1) a lack of fine-grained perception across disparate
> images, and (2) a diminished capability to effectively reason over and
> synthesize information from multiple visual inputs. However, while various
> prompting methods aim to describe visual content, many existing studies focus
> primarily on single-image settings or specific, constrained scenarios. This
> leaves a critical gap in understanding and addressing how MLLMs tackle more
> general and complex multi-image reasoning tasks. Thus, we first extensively
> investigate how current prompting methods perceive fine-grained visual details
> and process visual information when dealing with multiple images. Our findings
> reveal that existing prompting methods fall short in attending to needed clues
> and seamlessly integrating perception and reasoning. Inspired by the findings,
> we propose a new zero-shot prompting method, Question-Guided Chain-of-Captions
> (QG-CoC), a generalized prompting approach that effectively handles problems
> with an arbitrary number of images. We evaluate our method on various
> open-source and closed-source MLLMs for multi-image and single-image
> benchmarks. Experimental results indicate that QG-CoC demonstrates competitive
> performance across tasks and exhibits robust improvements in the challenging
> scenarios where existing prompting methods fail.

