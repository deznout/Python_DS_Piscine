import analytics
import config


def report():
    res = analytics.Research(config.file)
    try:
        analyze = analytics.Analytics(res.file_reader())
    except Exception as ex:
        print(ex)
    else:
        counts = analyze.counts()
        fractions = analyze.fractions()
        predict = analyze.predict_random(config.num_of_steps)

        tails_pred = sum(map(lambda x: int(x[1]), predict))
        heads_pred = sum(map(lambda x: int(x[0]), predict))
        tails_pred = str(tails_pred) + (" tails" if tails_pred != 1 else " tail")
        heads_pred = str(heads_pred) + (" heads" if heads_pred != 1 else " head")

        report_text = config.report.format(observ_count=sum(counts),
                                           tails_count=counts[1], heads_count=counts[0],
                                           tails_chance=fractions[1], heads_chance=fractions[0],
                                           num_of_steps=config.num_of_steps,
                                           tails_pred=tails_pred, heads_pred=heads_pred)

        analyze.save_file(report_text, 'report', 'txt')


if __name__ == '__main__':
    report()
